from app.database.models import User
from aiogram.types import Message


# real_user_id = Message.from_user.id
# user = User.get(User.user_id == real_user_id)
# lvl_user = user.user_lvl

def ff(lvl_user):
    base = 100

    # Расчет опыта для следующего уровня
    exp = base * (1.5 ** (lvl_user - 1))
    return int(exp)