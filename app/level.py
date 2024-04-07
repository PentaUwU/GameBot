from app.database.models import User
from aiogram.types import Message


# real_user_id = Message.from_user.id
# user = User.get(User.user_id == real_user_id)
# lvl_ = user.user_lvl

def ff(lvl_user):
    base = 100

    # Расчет опыта для следующего уровня
    exp = base * (1.5 ** (lvl_user - 1))
    return int(exp)

def lvl_plus(xp_user, lvl_user):
    if ff(lvl_user) - xp_user <= 0:
        lvl_user += 1
    return lvl_user