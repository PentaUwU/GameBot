from aiogram import F
from app import router
from aiogram.types import CallbackQuery, Message
from app.database.models import User
import app.keyboards as kb
from app.level import ff, lvl_plus



@router.callback_query(F.data == 'btn_top')
async def top_play(callback: CallbackQuery):
    user = User.select().where(User.user_id == callback.from_user.id).first()
    #Определяет new_level чтобы в переменной был просто нови уровень типочка
    new_level = lvl_plus(user.user_xp, user.user_lvl)
    while user.user_xp >= ff(new_level):
        new_level += 1
    #Если новый уровень из цикла блять больше пользовательского просто заменяет его в бд
    if new_level > user.user_lvl:
        user.user_lvl = new_level
        user.save()
    users = User.select().order_by(User.user_lvl.desc).limit(2)
    
    
    # user_list = [users]

    for user in users:
        await callback.message.edit_text(f'1) {user.username}{user.user_lvl}', reply_markup=kb.kb_back)