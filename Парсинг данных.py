import requests
from bs4 import BeautifulSoup

try:
    f = open('Парсинг.txt', 'w')
    url = "https://ru.wikipedia.org/wiki/Python"

    zagruzka = requests.get(url)

    if zagruzka.status_code == 200:
        print("Страница загружена!")
        f.write(f"Данные из сайта {url} \n")
        sop = BeautifulSoup(zagruzka.text, "html.parser")
        h3 = sop.find_all("h3")
        for i in h3:
            f.write(i.get_text())
            f.write("\n")
        print("Данные успешно загружены в файл")
    else:
        print("Ошибка загрузки страницы:", zagruzka.status_code)
    f.close()
except:
    print("Ошибка открытия файла")