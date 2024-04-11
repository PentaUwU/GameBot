from app import router
from aiogram import F, Bot
from aiogram.types import CallbackQuery, Message
from app.database.models import User, Group
import app.keyboards as kb
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from config import TOKEN

@router.callback_query(F.data == 'btn_back_group')
@router.callback_query(F.data == 'btn_decline_create')
@router.callback_query(F.data == 'btn_group')
async def group(callback: CallbackQuery):
    user = User.select().where(User.user_id == callback.from_user.id).first()
    if user.group_name == None:
        await callback.answer('')
        await callback.message.edit_text('Вы не состоите не в какой из групп. Вы можете присоедениться к любой группе из списка или создать свою.',
                                         reply_markup=kb.kb_withoutgroup)
    else:
        await callback.answer('')
        await callback.message.edit_text(f'Вы состоите в группе: {user.group_name}.',
                                         reply_markup=kb.kb_ingroup)

class GroupCreate(StatesGroup):
    name = State()

@router.callback_query(F.data == 'btn_create_group')
async def creategroup(callback: CallbackQuery, state: FSMContext):
    await callback.answer('')
    await state.set_state(GroupCreate.name)
    await callback.message.edit_text('Цена создания группы - 50.000$, если вы согласы напишите название группы.')
    
@router.message(GroupCreate.name)
async def creategroup_second(message: Message, state: FSMContext):
    await state.update_data(name = message.text)
    name = await state.get_data()
    await message.answer(f"Подтвердите создание группы с названием {name['name']}. После подтверждения с вас спишется 50.000$",
                         reply_markup=kb.kb_creategroup)

@router.callback_query(F.data == 'btn_accept_create')
async def creategroup_third(callback: CallbackQuery, state: FSMContext):
    user = User.select().where(User.user_id == callback.from_user.id).first()
    if user.balance >= 50000:
        name = await state.get_data()
        user.balance -= 50000
        group, created = Group.get_or_create(group_name=name['name'])
        user.group_name = group
        user.save()
        await callback.answer('')
        await callback.message.edit_text('Группа успешно создана.',
                                         reply_markup=kb.kb_back_group)
    else:
        await callback.answer('')
        await callback.message.edit_text('У вас недоставточно средств.',
                                         reply_markup=kb.kb_back_group)


  
