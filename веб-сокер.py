import aiohttp
import asyncio
import re

f = open('rt.txt', 'w')
zagolovok = r'<h1>(.*?)</h1>'
selka = r'href="(.*?)"'
with open('file.txt', 'w'):
    pass
async def otkr(url):
    try:
        async with aiohttp.ClientSession() as session:
            response = await session.get(url)
            content = await response.text()
            print(content)
            f.write(f"Ссылка:{url}")
            f.write("\n")
            zal = re.findall(zagolovok, content)
            f.write(f"Заголовок страницы:{zal}")
            f.write("\n")
            zal = re.findall(selka, content)
            f.write(f"Ссылки в странице страницы:{zal}")
            f.write("\n")
    except ValueError:
        async with aiohttp.ClientSession() as session:
            response = await session.get(url)
            content = await response.text()
            print(content)
            f.write(f"Ссылка:{url}")
            f.write("\n")
            zal = re.findall(zagolovok, content)
            f.write(f"Заголовок страницы:{zal}")
            f.write("\n")
            zal = re.findall(selka, content)
            f.write(f"Ссылки в странице страницы:{zal}")
            f.write("\n")
print("Пример:http://example.com")
url = input("Ссылка на страницу которую надо открыть 1:")
url1 = input("Ссылка на страницу которую надо открыть 2:")
asyncio.run(otkr(url))
asyncio.run(otkr(url1))
f.close()