from config_OWM import API_KEY
from pprint import pprint
import requests
import datetime

def get_weather(city, API_KEY):
    """Function only to check the work capacity of openweathermap API
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
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        )
        data = r.json()
        pprint(data)
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
        print(f"    {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
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
        
        
    except Exception as ex:
        print(ex)
        print("Перевірте назву вашого міста: ")
    
    
def main():
    """func for starting and working the program
    """
    city = input("Введіть назву міста:) ")
    get_weather(city, API_KEY)


if __name__ == '__main__':
    main()
