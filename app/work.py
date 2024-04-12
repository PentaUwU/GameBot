from app.database.models import Work, User
from aiogram import F
from aiogram.types import Message, CallbackQuery
from datetime import datetime,timedelta
from . import router
import app.keyboards as kb
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder



kb_jobjob = InlineKeyboardBuilder()


def keyboard_job():
    global kb_jobjob
    
    for i in kb.button_for_job:
        kb_jobjob.add(InlineKeyboardButton(text = i['name'], callback_data=i['call']))
        @router.callback_query(F.data == i['call'])
        async def start(callback: CallbackQuery):
            await callback.message.answer('')
            await callback.message.edit_text('Выберите работу:', reply_markup=kb_jobjob)







# @router.callback_query(F.data == 'btn_work')
# async def work_menu(callback: CallbackQuery):
#     await callback.answer('')
#     await callback.message.edit_text('Выберите работу:', reply_markup=kb.kb_work) 

# @router.callback_query(F.data == 'btn_work1')
# async def work1(callback: CallbackQuery):
#     await callback.answer('')
#     await callback.message.edit_text('''Вы выбрали работу "Добыча руды".
# Награда: 1000 долларав.
# Время выполнения: 1 час.
# Начать работу?
# ''', reply_markup=kb.kb_creategroup)
    
# @router.callback_query(F.data == 'btn_accept_create')
# async def work_accept(callback: CallbackQuery):
#     await callback.answer('')
#     user = User.select().where(User.user_id == callback.from_user.id).first()
#     if datetime.now() - user.time_work > timedelta(hours=1):
#         user.time_work = datetime.now()
#         user.balance += 1000
#         user.save()
#         await callback.message.edit_text('Возвращайтесь через час')
#     else:
#         await callback.message.edit_text('Час не прошел')