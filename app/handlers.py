from aiogram import F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from app import router
from app.database.models import User
from typing import Union
from datetime import timedelta, datetime
from app.level import *
import app.keyboards as kb

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

# Вывод информации о пользователе и логика добавления уровня при заходе на профиль
@router.callback_query(F.data == "btn_profile")
async def profile(callback: CallbackQuery):

    #Определяет user(как я понял эту хуйню везде придется прописивать, потому что оно хранит информацию из бд всю)
    user = User.select().where(User.user_id == callback.from_user.id).first()
    
    #Определяет new_level чтобы в переменной был просто нови уровень типочка
    new_level = lvl_plus(user.user_xp, user.user_lvl)
    
    #Проверяет пока уровень пользователя не будет больше или равен нужному для перехода и добавляет 1 к уровню
    while user.user_xp >= ff(new_level):
        new_level += 1
    
    #Если новый уровень из цикла блять больше пользовательского просто заменяет его в бд
    if new_level > user.user_lvl:
        user.user_lvl = new_level
        user.save()
    
    await callback.answer('')
    await callback.message.edit_text(f"""Твой id: {user.id}.
У тебя на счету: {user.balance}$
Твой уровень: {new_level}
Опыта до нового уровня: {ff(new_level) - user.user_xp}""",
                                    reply_markup= kb.kb_back)

#НАКРУТКА
@router.callback_query(F.data == 'btn_cheat')
async def cheat(callback: CallbackQuery):
    user = User.select().where(User.user_id == callback.from_user.id).first()
    user_pidor_cheater = user.user_xp + 1000
    user.user_xp = user_pidor_cheater
    user.save()
    await callback.answer('Вы пидорас! УРА')

#Это я закоментил на всякий вдруг чтот наебнулось бы :)
# @router.callback_query(F.data == "btn_profile")
# async def profile(callback: CallbackQuery):
#     user = User.select().where(User.user_id == callback.from_user.id).first()
#     await callback.answer('')
#     await callback.message.edit_text(f"""Твой id: {user.id}.
# У тебя на счету: {user.balance}$
# Твой уровень: {lvl_plus(user.user_xp, user.user_lvl)}
# Опыта до нового уровня: {ff(user.user_lvl) - user.user_xp}""",
#                                     reply_markup= kb.kb_back)
    
# Ежедневный бонус
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
        remaining_time = user.last_bonus_claim + timedelta(hours=24) - datetime.now()
        # Форматируем временной интервал
        remaining_time_formatted = str(remaining_time).split('.')[0]
        await callback.message.edit_text(f"Сегодня ты уже получал бонус, приходи через: {remaining_time_formatted}",
                                             reply_markup=kb.kb_back)
        