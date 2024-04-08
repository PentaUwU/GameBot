from app import router 
from datetime import datetime, timedelta
from aiogram import F
from aiogram.types import CallbackQuery
from app.database.models import User
import app.keyboards as kb

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