from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton)



#-----------------------------------КНОПКИ-----------------------------
#Кнопка назад
btn_back = InlineKeyboardButton(text='Вернуться назад', callback_data='btn_back')

#Кнопки вступления
btn_profile =  InlineKeyboardButton(text='Профиль', callback_data='btn_profile')
btn_top =  InlineKeyboardButton(text='Топ игроков', callback_data='btn_top')
btn_daily_bonus =  InlineKeyboardButton(text='Ежедневный бонус', callback_data='btn_daily_bonus')
btn_swag4 =  InlineKeyboardButton(text='Хуй', callback_data='btn_swag4')
# btn_swag5 =  InlineKeyboardButton(text='Хуй', callback_data='btn_swag5')

#Кнопка накрутки уровня для проверки
btn_cheat = InlineKeyboardButton(text='💉НАКРУТКА', callback_data='btn_cheat')

#-----------------------------------КЛАВИАТУРЫ-----------------------------------
#Клавиатура вступления
kb_back = InlineKeyboardMarkup(inline_keyboard=[[btn_back]])
kb_main = InlineKeyboardMarkup(inline_keyboard=[[btn_profile, btn_daily_bonus],[btn_top],[btn_cheat]])
