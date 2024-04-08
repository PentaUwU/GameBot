def next_xp(lvl_user):
    base = 100

    # Расчет опыта для следующего уровня
    exp = base * (1.5 ** (lvl_user - 1))
    return int(exp)

def lvl_plus(xp_user, lvl_user):
    if next_xp(lvl_user) - xp_user <= 0:
        lvl_user += 1
    return lvl_user