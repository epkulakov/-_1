from datetime import datetime
import random
import asyncio
import psycopg2
nomer = []
try:
    connection = psycopg2.connect(
        user="postgres",
        password="9787061",
        host="127.0.0.1",
        port="5432",
        database="DatBASE"
    )
    cursor = connection.cursor()
    select_query = 'SELECT * FROM emploes;'
    cursor.execute(select_query)
    records = cursor.fetchall()
    i = 0
    for row in records:
            globals()[f'var_{i}'] = [int(row[0]),int(row[1]),row[2],int(row[3])]
            nomer.append(row[0])
            print(row)
            i += 1
    d = i - 1
except Exception as error:
    print("Ошибка", error)
finally:
    if connection:
        cursor.close()
        connection.close()
async def yt(name):
    print(f"Началось {name}")
    await asyncio.sleep(name[3])
    print(f"Завершилось {name}")

def sortirovka(arr):
    if len(arr) <= 1:
        return arr
    sr = arr[len(arr) // 2]
    left = [x for x in arr if x < sr]
    mid = [x for x in arr if x == sr]
    rig = [x for x in arr if x > sr]
    return sortirovka(left) + mid + sortirovka(rig)
def poisk():
    p = int(input('Напишите ID задачи которую хотите найти:'))
    for i in range(d + 1):
        if globals()[f'var_{i}'] != []:
            if globals()[f'var_{i}'][0] == p:
                return globals()[f'var_{i}']
    return 'Элемент не найден'
def new_id():
        nom = random.randint(100, 999999)
        for i in range(d + 1):
            if nomer[i] == nom:
                new_id()
        return nom
def udal(e):
    global nomer
    for i in range(d + 1):
        if globals()[f'var_{i}'] != []:
            if globals()[f'var_{i}'][0] == e:
                nomer.insert(i,0)
                globals()[f'var_{i}'] = []
                return 'Элемент успешно удалён'
    return 'Элемент не найден и не удалён'


print("Я помощник для управления задачами")
while True:
    print("Выбери действие ")
    print('''
    1-Добавление новой задачи в список.
    2-Удаление задачи по её идентификатору.
    3-Запуск всех задач (асинхронно).
    4-Просмотр списка задач.
    5-Поиск задачи по идентификатору.
    6-выход
    ''')
    vebor = int(input('Выбери номер действия:'))
    if vebor == 1:
        zada = input("Что имено будет выполняться в этой задаче?")
        time = datetime.now().time()
        vrem = random.randint(1, 8)
        rial_time = int(time.strftime("%H"))
        r = new_id()
        d += 1
        nomer.append(r)
        globals()[f'var_{d}'] = [r,rial_time,zada,vrem]
    elif vebor == 2:
        e = int(input("Введите ID задачи которую хотите удалить?"))
        print(udal(e))
    elif vebor == 3:
        for i in range(d + 1):
            if globals()[f'var_{i}'] != []:
                 e = globals()[f'var_{i}']
                 asyncio.run(yt(e))
    elif vebor == 4:
        arr = []
        for p in range(d + 1):
            if globals()[f'var_{p}'] != []:
                arr.append(globals()[f'var_{p}'][1])
        w = sortirovka(arr)
        for t in range(len(w)):
            p = 0
            while p == 0:
                for u in range(d + 1):
                    if globals()[f'var_{u}'] != []:
                        if w[t] == globals()[f'var_{u}'][1]:
                            print(globals()[f'var_{u}'])
                            p += 1
    elif vebor == 5:
        print(poisk())
    elif vebor == 6:
        nolu = "TRUNCATE TABLE emploes;"
        try:
            connection = psycopg2.connect(
                user="postgres",
                password="9787061",
                host="127.0.0.1",
                port="5432",
                database="DatBASE"
            )
            cursor = connection.cursor()
            cursor.execute(nolu)
            insert_query: str = '''
                 INSERT INTO emploes (id,time,name,vrem)
                 VALUES (%s, %s, %s, %s);
                 '''
            for i in range(d + 1):
                if globals()[f'var_{i}'] != []:
                    dan = globals()[f'var_{i}']
                    cursor.execute(insert_query, dan)
                    connection.commit()
            print("Данные успешно сохранены в таблицу 'emploes'")
        except Exception as error:
            print("Ошибка при подключении к серверам", error)
        quit()

