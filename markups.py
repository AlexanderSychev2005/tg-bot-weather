from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
"""File for creating the buttons for tg bot 
"""
btnMain = KeyboardButton('Головне меню')
subscribe_time = KeyboardButton('Підписка час')
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(subscribe_time)
