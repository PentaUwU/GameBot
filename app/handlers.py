from aiogram import F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from app import router
import app.keyboards as kb
from app.database.models import User
from typing import Union
from datetime import timedelta, datetime

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


@router.callback_query(F.data == "btn_profile")
async def profile(callback: CallbackQuery):
    user = User.select().where(User.user_id == callback.from_user.id).first()
    await callback.answer('')
    await callback.message.edit_text(f"""Твой id: {user.id}.
У тебя на счету: {user.balance}$""",
                                    reply_markup= kb.kb_back)

@router.callback_query(F.data == 'btn_daily_bonus')
async def dailybonus(callback: CallbackQuery):
    user = User.select().where(User.user_id == callback.from_user.id).first()
    if datetime.now() - user.last_bonus_claim > timedelta(hours=24):
        user.last_bonus_claim = datetime.now()
        user.balance += 50000
        user.save()  # Сохраняем изменения в базе данных
        await callback.answer('Бонус успешно получен')
    else:
        # Вычисляем разницу времени
        remaining_time = user.last_bonus_claim + timedelta(hours=24) - datetime.now
        # Форматируем временной интервал
        remaining_time_formatted = str(remaining_time).split('.')[0]
        await callback.message.edit_text(f"Сегодня ты уже получал бонус, приходи через: {remaining_time_formatted}",
                                             reply_markup=kb.kb_back)
        