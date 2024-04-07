from aiogram import F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from app import router
# from typing import Union

# Команда старт
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'{message.from_user.first_name}, ку брат')