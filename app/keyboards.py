from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton)
from .database.models import Work


#-----------------------------------КНОПКИ-----------------------------
#Кнопка назад
btn_back = InlineKeyboardButton(text='Вернуться назад', callback_data='btn_back')
btn_back_profile = InlineKeyboardButton(text = "Вернуться назад", callback_data='btn_back_profile')
btn_back_group = InlineKeyboardButton(text = 'Вернуться назад', callback_data='btn_back_group')

#Кнопки вступления
btn_profile =  InlineKeyboardButton(text='Профиль', callback_data='btn_profile')
btn_top =  InlineKeyboardButton(text='Топ игроков', callback_data='btn_top')
btn_daily_bonus =  InlineKeyboardButton(text='Ежедневный бонус', callback_data='btn_daily_bonus')
btn_top_lvl =  InlineKeyboardButton(text='➡️', callback_data='btn_top_lvl')
btn_top_balance =  InlineKeyboardButton(text='⬅️', callback_data='btn_top_balance')
btn_transfer = InlineKeyboardButton(text = "Перевод денег", callback_data="btn_transfer")
btn_group = InlineKeyboardButton(text = "Меню групп", callback_data='btn_group')
btn_back_transfer = InlineKeyboardButton(text="Вернуться назад", callback_data= "btn_transfer")
btn_create_group = InlineKeyboardButton(text="Создать группу", callback_data='btn_create_group')
btn_join_group = InlineKeyboardButton(text="Вступить в группу", callback_data='btn_join_group')
btn_menu_group = InlineKeyboardButton(text="Меню группы", callback_data='btn_menu_group')
btn_accept_create = InlineKeyboardButton(text='Подтвердить', callback_data='btn_accept_create')
btn_decline_create = InlineKeyboardButton(text='Отказаться', callback_data='btn_decline_create')

#Кнопка накрутки уровня для проверки
btn_cheat = InlineKeyboardButton(text='💉НАКРУТКА', callback_data='btn_cheat')

#Кнопка подтверждения
btn_confirm = InlineKeyboardButton(text='Подтвердить', callback_data='btn_confirm')

#Кнопка работы
btn_work = InlineKeyboardButton(text='Работа', callback_data='btn_work')

#Кнопки работ
class Keyboards:
    def __init__(self, Work):
        pass
    def work(self):
        keyboard = InlineKeyboardMarkup(row_width = 2)
        keyboard.add(
            InlineKeyboardButton (text=f'{Work.work_name}')
        )
# btn_work1 = InlineKeyboardButton(text='Шахта', callback_data='btn_work1')
#-----------------------------------КЛАВИАТУРЫ-----------------------------------
#Клавиатура вступления
kb_back = InlineKeyboardMarkup(inline_keyboard=[[btn_back]])
kb_main = InlineKeyboardMarkup(inline_keyboard=[[btn_profile, btn_daily_bonus],[btn_top, btn_work],[btn_cheat]])
kb_top_balance = InlineKeyboardMarkup(inline_keyboard=[[btn_back, btn_top_lvl]])
kb_top_lvl = InlineKeyboardMarkup(inline_keyboard=[[btn_top_balance, btn_back]])
kb_profile = InlineKeyboardMarkup(inline_keyboard=[[btn_transfer, btn_back, btn_group]])
kb_transfer =InlineKeyboardMarkup(inline_keyboard=[[btn_back_profile]])
kb_back_transfer = InlineKeyboardMarkup(inline_keyboard=[[btn_back_transfer]])
kb_confirm = InlineKeyboardMarkup(inline_keyboard=[[btn_confirm, btn_back_transfer]])
# kb_work = InlineKeyboardMarkup(inline_keyboard=[[]])
kb_ingroup = InlineKeyboardMarkup(inline_keyboard=[[btn_menu_group]])
kb_withoutgroup = InlineKeyboardMarkup(inline_keyboard=[[btn_join_group, btn_create_group]])
kb_creategroup = InlineKeyboardMarkup(inline_keyboard=[[btn_accept_create, btn_decline_create]])
kb_back_group = InlineKeyboardMarkup(inline_keyboard=[[btn_back_group]])
