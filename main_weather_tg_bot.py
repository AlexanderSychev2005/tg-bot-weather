import requests
import datetime
from config_OWM import tg_bot_token, API_KEY
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import markups as nav
import time

async def on_start(_):
    """Function arises at the program start 

    Args:
        _ : _Any arg just for work_
    """
    print("Bot started!")

bot = Bot(token= tg_bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])     
async def start_command(messege: types.Message):
    """message, that bot write after we entered command 'start'
    async  = function in program
    Await  = print
    """
    await messege.reply("Привіт! Ти можеш написати своє місто і я тобі пришлю оновлену погоду)", reply_markup = nav.mainMenu)
    
        
@dp.message_handler() 
async def get_weather(messege: types.Message):
    """program checks every word we typed in it and return a result depends on typing

    Args:
        messege (types.Message): represents a message
    """
    if messege.text == "Підписка час":
        await messege.reply("Введи час в який ти хочеш отримувати прогноз погоди:")

        
    else:
        """unicode emojis for program depends on weather
        """
        code_to_smiles = {
            "Clear" : "Ясно \U0001F31E",
            "Clouds" : "Хмарно \U00002601",
            "Rain": "Дощить \U0001F327",
            "Drizzle": "Морось \U00002614", 
            "Thunderstorm": "Гроза \U000026C8", 
            "Snow": "Сніг \U00002744",
            "Mist": "Туман \U0001F32B"
        }
        """function checks our input , if it's city , func return a weather result to that city, if not , ask again input
        """
        try:
            r = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?q={messege.text}&appid={API_KEY}&units=metric"
            )
            data = r.json()
            #pprint(data)
            city = data["name"]

            weather_description = data["weather"][0]["main"]
            if weather_description in code_to_smiles:  #Перевіряємо, чи є значення в ключах dict
                wd = code_to_smiles[weather_description]
            else:
                wd = "Не можу зрозуміти, зразу з ліжка не видно, подивись у вікно що там))"
            cur_weather = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]
            wind = data["wind"]["speed"]
            pressure = data["main"]["pressure"]
            sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
            sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
            length_of_the_day = sunset_timestamp - sunrise_timestamp
            await messege.reply(f"    {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
                f"Погода в місті: {city}\n"
                f"Температура: {cur_weather}°C {wd}\n" 
                f"Почувається як: {feels_like}\n"
                f"Вологість: {humidity}\n"
                f"Тиск: {pressure} мм рт.ст.\n"
                f"Вітер {wind} м/с\n"
                f"Схід сонця: {sunrise_timestamp}\n"
                f"Захід сонця: {sunset_timestamp}\n"
                f"Довжина дня: {length_of_the_day}\n"
                f"Гарного дня!")
        except :
            await messege.reply("Перевірте назву вашого міста: ")

 
    
"""generate start of bot 
"""
if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_start)