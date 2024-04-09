from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton)



#-----------------------------------КНОПКИ-----------------------------
#Кнопка назад
btn_back = InlineKeyboardButton(text='Вернуться назад', callback_data='btn_back')
btn_back_profile = InlineKeyboardButton(text = "Вернуться назад", callback_data='btn_back_profile')

#Кнопки вступления
btn_profile =  InlineKeyboardButton(text='Профиль', callback_data='btn_profile')
btn_top =  InlineKeyboardButton(text='Топ игроков', callback_data='btn_top')
btn_daily_bonus =  InlineKeyboardButton(text='Ежедневный бонус', callback_data='btn_daily_bonus')
btn_top_lvl =  InlineKeyboardButton(text='➡️', callback_data='btn_top_lvl')
btn_top_balance =  InlineKeyboardButton(text='⬅️', callback_data='btn_top_balance')
btn_transfer = InlineKeyboardButton(text = "Перевод денег", callback_data="btn_transfer")
btn_back_transfer = InlineKeyboardButton(text="Вернуться назад", callback_data= "btn_transfer")

#Кнопка накрутки уровня для проверки
btn_cheat = InlineKeyboardButton(text='💉НАКРУТКА', callback_data='btn_cheat')

#-----------------------------------КЛАВИАТУРЫ-----------------------------------
#Клавиатура вступления
kb_back = InlineKeyboardMarkup(inline_keyboard=[[btn_back]])
kb_main = InlineKeyboardMarkup(inline_keyboard=[[btn_profile, btn_daily_bonus],[btn_top],[btn_cheat]])
kb_top_balance = InlineKeyboardMarkup(inline_keyboard=[[btn_back, btn_top_lvl]])
kb_top_lvl = InlineKeyboardMarkup(inline_keyboard=[[btn_top_balance, btn_back]])
kb_profile = InlineKeyboardMarkup(inline_keyboard=[[btn_transfer, btn_back]])
kb_transfer =InlineKeyboardMarkup(inline_keyboard=[[btn_back_profile]])
kb_back_transfer = InlineKeyboardMarkup(inline_keyboard=[[btn_back_transfer]])
