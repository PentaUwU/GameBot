from aiogram import F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from app import router
from app.database.models import User
# from typing import Union
#
# Команда старт
@router.message(CommandStart())
async def cmd_start(message: Message):
    # Запись информации о новых пользователях в базу данных
    users, created = User.get_or_create(user_id = message.from_user.id,
                                        username = message.from_user.username)
    users.save()
    await message.reply(f'{message.from_user.first_name}, ку брат')