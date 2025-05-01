import psycopg2
try:
    connection = psycopg2.connect(
        user="postgres",
        password="9787061",
        host="127.0.0.1",
        port="5432",
        database="DatBASE"
    )
    cursor = connection.cursor()
    select_query = 'SELECT * FROM student;'
    cursor.execute(select_query)
    records = cursor.fetchall()
    i = 0
    for row in records:
            globals()[f'student_{i}'] = [row[0],row[1],int(row[2]),int(row[3])]
            print(globals()[f'student_{i}'])
            print(row)
            i += 1
    d = i - 1
except Exception as error:
    print("Ошибка", error)
finally:
    if connection:
        cursor.close()
        connection.close()



print("Я помощник для учёта студентов")
while True:
    print("Выбери действие ")
    print('''
    1-Добавление нового студента.
    2-Удаление студента из учёта.
    3-Изменение данных о студенте.
    4-Просмотр списка студентов.
    5-выход
    ''')
    vebor = int(input('Выбери номер действия:'))
    if vebor == 1:
        name = input("Какое ваше имя ?")
        fam = input("Какая у вас фамилия ?")
        nom = int(input("На каком вы курсе?"))
        year = int(input("Какой у вас возраст ?"))
        while year < 18:
            print("Возраст не может быть меньше 18!")
            year = int(input("Какой у вас возраст ?"))
        d += 1
        globals()[f'student_{d}'] = [name,fam,nom,year]
    elif vebor == 2:
        for i in range(d + 1):
            if globals()[f'student_{i}'] != []:
              print(f"{i}  {globals()[f'student_{i}']} ")
        e = int(input("Введите номер студента которого хотите удалить?"))
        print(f"Вы удалили {globals()[f'student_{e}']}")
        globals()[f'student_{e}'] = []

    elif vebor == 3:
        for i in range(d + 1):
            if globals()[f'student_{i}'] != []:
                print(f"{i}  {globals()[f'student_{i}']} ")
        e = int(input("Введите номер студента у которого хотите изменить данные?"))
        print(globals()[f'student_{e}'])
        r = int(input("""Что именно хотите изменить ?
        0 - имя ; 1 - фамилия ; 2 - номер курса ; 3 - возраст """))
        u = input("На что именно хотите изменить ?")
        globals()[f'student_{e}'][r] = u

    elif vebor == 4:
        for i in range(d + 1):
            if globals()[f'student_{i}'] != []:
                print(f"{i}  {globals()[f'student_{i}']} ")
    elif vebor == 5:
        nolu = "TRUNCATE TABLE student;"
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
                 INSERT INTO student (name,famil,nomer,year)
                 VALUES (%s, %s, %s, %s);
                 '''
            for i in range(d + 1):
                if globals()[f'student_{i}'] != []:
                    dan = globals()[f'student_{i}']
                    cursor.execute(insert_query, dan)
                    connection.commit()
            print("Данные успешно сохранены в таблицу 'student'")
        except Exception as error:
            print("Ошибка при подключении к серверам", error)
        quit()