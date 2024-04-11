from app.database.models import Work, User
from aiogram import F
from aiogram.types import Message, CallbackQuery
from . import router
import app.keyboards as kb


@router.callback_query(F.data == 'btn_work')
async def work_menu(callback: CallbackQuery):
    await callback.answer('')
    keyboard = kb.kb_work
    await callback.message.answer('Выберите работу:', reply_markup=keyboard) 

# @router.callback_query(F.data == 'btn_work1')
# async def work1(callback: CallbackQuery):
#     await callback.answer('')
#     await callback.message.answer('''Вы выбрали работу "Добыча руды".
# Награда: 10 золотых монет.
# Время выполнения: 1 час.
# Начать работу?
# [Да] [Нет]
# ''')