from aiogram import F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from app import router
import app.keyboards as kb
from app.database.models import User
from typing import Union
# Привет
# Команда старт
@router.callback_query(F.data == 'btn_back')
@router.message(CommandStart())
async def cmd_start(message: Union[Message, CallbackQuery]):
    # Запись информации о новых пользователях в базу данных
    users, created = User.get_or_create(user_id = message.from_user.id,
                                        username = message.from_user.username)                                                  
    users.save()
    if isinstance(message, CallbackQuery): # возвращение в галвное меню кнопкой 'Вернуться назад'
        await message.answer('')
        await message.message.edit_text(f"{message.from_user.first_name}, когда деньги заработаеш уже?",
                                        reply_markup=kb.kb_main)
        
    else: # Сообщение при вводе команды /start
        await message.reply(f'Привет, {message.from_user.first_name}, приятной игры!',
                                    reply_markup=kb.kb_main)