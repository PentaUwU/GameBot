from aiogram import F
from aiogram.types import  CallbackQuery
from app import router
from app.database.models import User
from app.level import ff, lvl_plus



#НАКРУТКА
@router.callback_query(F.data == 'btn_cheat')
async def cheat(callback: CallbackQuery):
    user = User.select().where(User.user_id == callback.from_user.id).first()
    #Определяет new_level чтобы в переменной был просто нови уровень типочка
    new_level = lvl_plus(user.user_xp, user.user_lvl)
    while user.user_xp >= ff(new_level):
        new_level += 1
    #Если новый уровень из цикла блять больше пользовательского просто заменяет его в бд
    if new_level > user.user_lvl:
        user.user_lvl = new_level
        user.save()
    await callback.answer('')

    user = User.select().where(User.user_id == callback.from_user.id).first()
    user_pidor_cheater = user.user_xp + 1000
    user.user_xp = user_pidor_cheater
    user.save()
    await callback.answer('Вы пидорас! УРА')


    

        