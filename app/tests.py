from aiogram import F
from aiogram.types import  CallbackQuery
from app import router
from app.database.models import User



#НАКРУТКА
@router.callback_query(F.data == 'btn_cheat')
async def cheat(callback: CallbackQuery):
    user = User.select().where(User.user_id == callback.from_user.id).first()
    user_pidor_cheater = user.user_xp + 1000
    user.user_xp = user_pidor_cheater
    user.save()
    await callback.answer('Вы пидорас! УРА')


    

        