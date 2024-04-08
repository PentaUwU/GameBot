from aiogram import F
from app import router
from aiogram.types import CallbackQuery, Message
from app.database.models import User
import app.keyboards as kb



@router.callback_query(F.data == 'btn_top')
async def top_play(callback: CallbackQuery):
    users = User.select().order_by(User.user_lvl.desc).limit(2)
    
    # user_list = [users]

    for user in users:
        await callback.message.edit_text(f'1) {user.username}{user.user_lvl}', reply_markup=kb.kb_back)