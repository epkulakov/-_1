import requests
import csv

pogoda = ["Москва", "Нью-Йорк", "Токио", "Лондон", "Берлин"]

API_KEY = 'b747f919-6e92-40bf-9dc9-f30287cdbe91'

hirota = [55.751244,40.7143,35.6895,51.50853,52.5244]
dolgota = [37.618423, -74.006,139.69171,-0.12574,13.4105]

url = 'https://api.weather.yandex.ru/v2/forecast?lat=52.37125&lon=4.89388'

sr = 0
smal_temp = 100
max_temp = 0

table = [['Город','Температура','Облачность','Давление','Чуствуется как','Скорость ветра']]
stroka = []

f = open('Данные о погодею.csv', mode='w', newline='')

try:
    for i in range(len(pogoda)):
        stroka = []

        params = {
            'lat': hirota[i],
            'lon': dolgota[i],
            'lang': 'ru_RU',
        }

        headers = {
            'X-Yandex-API-Key': API_KEY
        }
        response = requests.get(url, params=params, headers=headers)

        if response.status_code == 200:
            data = response.json()
            dan = data['fact']

            temp = dan['temp']
            oblak = dan['condition']
            davleni = dan['pressure_mm']
            ochukenia = dan['feels_like']
            veter = dan['wind_speed']

            stroka.append(pogoda[i])
            stroka.append(temp)
            stroka.append(oblak)
            stroka.append(davleni)
            stroka.append(ochukenia)
            stroka.append(veter)

            sr += temp

            if smal_temp > temp :
                smal_temp = temp
            if max_temp < temp:
                max_temp = temp

            print(f'Текущие погодные условия в {pogoda[i]}:')
            print(f'- Температура:{temp} C')
            print(f'- Облачность: {oblak}')
            print(f'- Давление: {davleni} ')
            print(f'- Чувствуется как:{ochukenia} C')
            print(f'- Скорость ветра: {veter} м/с')

            table.append(stroka)
        elif response.status_code == 500:
            print("Попробуйте перезапустить код")
        elif response.status_code == 403:
            print("Запрет доступа к ресурсу")
        elif response.status_code == 301:
            print("У страницы другой URL")
        else:
            print(f'Ошибка при подключении: {response.status_code}, {response.text}')
    sr = sr/i
    print(f"Самая низкая температура из городов {smal_temp}")
    print(f"Самая высокая температура из городов {max_temp}")
    print(f"Средняя температура среди всех городов: {sr}")
    writer = csv.writer(f)
    writer.writerows(table)
    print("Все данные успешно сохранены в таблицу")
except Exception as e:
    print(f'Возникла ошибка: {e}')