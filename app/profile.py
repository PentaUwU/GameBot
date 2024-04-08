from app import router
from app.level import next_xp, lvl_plus
from aiogram import F
from aiogram.types import CallbackQuery
from app.database.models import User
import app.keyboards as kb


@router.callback_query(F.data == "btn_back_profile")
@router.callback_query(F.data == "btn_profile")
async def profile(callback: CallbackQuery):

    #Определяет user(как я понял эту хуйню везде придется прописивать, потому что оно хранит информацию из бд всю)
    user = User.select().where(User.user_id == callback.from_user.id).first()
    
    #Определяет new_level чтобы в переменной был просто нови уровень типочка
    new_level = lvl_plus(user.user_xp, user.user_lvl)
    
    #Проверяет пока уровень пользователя не будет больше или равен нужному для перехода и добавляет 1 к уровню
    while user.user_xp >= next_xp(new_level):
        new_level += 1
    
    #Если новый уровень из цикла блять больше пользовательского просто заменяет его в бд
    if new_level > user.user_lvl:
        user.user_lvl = new_level
        user.save()
    
    await callback.answer('')
    await callback.message.edit_text(f"""Твой id: {user.user_id}.
У тебя на счету: {user.balance}$
Твой уровень: {new_level}
Опыта до нового уровня: {next_xp(new_level) - user.user_xp}""",
                                    reply_markup= kb.kb_profile)
    
@router.callback_query(F.data == "btn_transfer")
async def transfer(callback: CallbackQuery):
    user = User.select().where(User.user_id == callback.from_user.id).first()
    await callback.answer('')
    await callback.message.edit_text("Введите id пользователя, которому хотите перевести деньги:")
    userid = callback.message.text 
    # alabay = User.get(User.user_id == userid)
    await callback.message.answer(f"Вы ввели {userid}")