from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton)



#-----------------------------------КНОПКИ-----------------------------
#Кнопка назад
btn_back = InlineKeyboardButton(text='Вернуться назад', callback_data='btn_back')

#Кнопки главного меню
btn_swag =  InlineKeyboardButton(text='Хуй', callback_data='btn_swag')
btn_swag2 =  InlineKeyboardButton(text='Хуй', callback_data='btn_swag2')
btn_swag3 =  InlineKeyboardButton(text='Хуй', callback_data='btn_swag3')
btn_swag4 =  InlineKeyboardButton(text='Хуй', callback_data='btn_swag4')
btn_swag5 =  InlineKeyboardButton(text='Хуй', callback_data='btn_swag5')


#-----------------------------------КЛАВИАТУРЫ-----------------------------------
#Клавиатура главного меню
kb_main = InlineKeyboardMarkup([[btn_swag,btn_swag2], [btn_swag3, btn_swag4][btn_swag5]])
