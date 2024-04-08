from aiogram import F
from app import router
from aiogram.types import CallbackQuery, Message
from app.database.models import User
import app.keyboards as kb
from app.level import next_xp, lvl_plus



@router.callback_query(F.data == 'btn_top')
async def top_play(callback: CallbackQuery):
    # user = User.select().where(User.user_id == callback.from_user.id).first()
    # #Определяет new_level чтобы в переменной был просто нови уровень типочка
    # new_level = lvl_plus(user.user_xp, user.user_lvl)
    # while user.user_xp >= next_xp(new_level):
    #     new_level += 1
    # #Если новый уровень из цикла блять больше пользовательского просто заменяет его в бд
    # if new_level > user.user_lvl:
    #     user.user_lvl = new_level
    #     user.save()
    # await callback.answer('')

    top_balance_users = (User.select().order_by(User.balance.desc()).limit(10))

    message = "Топ игроков по балансу:\n"
    for i, user in enumerate(top_balance_users, start=1):
        message += f'{i}) {user.username} - Баланс: {user.balance}\n'

    # Получаем 10 пользователей с наибольшим опытом
    top_lvl_users = (User.select().order_by(User.user_lvl.desc()).limit(10))

    message += "\nТоп игроков по опыту:\n"
    for i, user in enumerate(top_lvl_users, start=1):
        message += f'{i}) {user.username} - Уровень: {user.user_lvl}\n'

    await callback.message.edit_text(message, reply_markup=kb.kb_back)