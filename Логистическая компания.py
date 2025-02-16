import heapq
import time
from datetime import datetime
print("Привет, я помощник для Логистической компании!")
print("")
var_0 = [12539,'Краснодар','Москва',4566,20,0]
var_1 = [10899,'Сочи','Питер',6200,10,0]
var_2 = [69539,'Екатеренбург','Москва',2000,22,1]
d = 2
while True:
    class Delivery():
        def start(d):
            pq = []
            name = []
            pr = []
            duration = []
            p = 0
            for i in range(d + 1):
                if globals()[f'var_{i}'] != []:
                   name.append(globals()[f'var_{i}'])
                   current_time = datetime.now().time()
                   clock_time = int(current_time.strftime("%H"))
                   if clock_time > globals()[f'var_{i}'][4]:
                      f = globals()[f'var_{i}'][4] + (24 - clock_time)
                   else:
                      f = globals()[f'var_{i}'][4] - clock_time
                   duration.append(f)
                   pr.append(globals()[f'var_{i}'][5])
                   heapq.heappush(pq, (pr[p], name[p]))
                   p += 1
            for i in range(d + 1 ):
                f = pr.index(min(pr))
                u = int(input(f"Реализовавать задачу {name[f]} 1 - да     2 - нет:"))
                pr[f] = 10000000000
                if u == 1:
                    o = duration[f]
                    y = heapq.heappop(pq)
                    for i in range(len(pq)):
                        print(f"На складе:{pq[i]}")
                    print(f"Достовляется: {y}")
                    time.sleep(o)
                    print(f"Завершоный: {y}")
                    print("")
        def vse(d):
            print('№     Откуда    Куда    Вес        К какому      Уровень важности')
            print('                      (в гаммах)  времени (Часы)       ')
            for i in range(d + 1):
                if globals()[f'var_{i}'] != []:
                      print(*globals()[f'var_{i}'])

            print("")
        def udal(d):
            v = 0
            for i in range(d + 1):
                if globals()[f'var_{i}'] != []:
                       print(v ,'   ',*globals()[f'var_{i}'])
                       v += 1
            ud = int(input('Ведите номер доставки которую хотите удалить:'))
            globals()[f'var_{ud}'] = []
            print("")
        def new():
            global d
            d += 1
            nom = int(input('Номер доставки(числа)?'))
            ot = input('От куда поедет доставка?')
            kud = input('Куда поедет доставка?')
            kilo = int(input("Какой вес доставки?"))
            hour = int(input('К какому времени должна подойти доставка (только часы)?'))
            if hour > 24:
                while hour > 24:
                    hour = int(input('К какому времени должна подойти доставка (только часы)?'))
            x = int(input('Ведите уровень важности 0 - срочный(число!), 1 - обычный'))
            globals()[f'var_{d}'] = [nom,ot,kud,kilo,hour,x]
            print("")
        def poisk(d):
            print('Поиск доставки по номеру')
            veb = int(input(('Введите номер доставки которую хотите найти:')))
            for v in range(d + 1):
                if globals()[f'var_{v}'] != []:
                   if globals()[f'var_{v}'][0] == veb:
                      print(*globals()[f'var_{v}'])
            print("")
        def poisk_v(arr,x):
                 left, right = 0, len(arr) - 1

                 while left <= right:
                     mid = (left + right) // 2
                     if arr[mid] == x:
                         return mid
                     elif arr[mid] < x:
                         left = mid + 1
                     else:
                         right = mid - 1
                 return -1
        def redak(d):
            v = 0
            l = []
            for i in range(d + 1):
                if globals()[f'var_{i}'] != []:
                    print(v, '   ', *globals()[f'var_{i}'])
                    l.append(i)
                    v += 1
            r = int(input('Ведите номер доставки которую хотите изменить:'))
            print(globals()[f'var_{l[r]}'])
            nom = int(input('Номер доставки(числа)?'))
            ot = input('От куда поедет доставка?')
            kud = input('Куда поедет доставка?')
            kilo = int(input("Какой вес доставки?"))
            hour = int(input('К какому времени должна подойти доставка (только часы)?'))
            if hour > 24:
                while hour > 24:
                    hour = int(input('К какому времени должна подойти доставка (только часы)?'))
            x = int(input('Ведите уровень важности 0 - Срочный, 1 - обычный'))
            globals()[f'var_{l[r]}'] = [nom, ot, kud, kilo, hour, x]
            print("")
        def vrem(g):
            if len(g) <= 1:
                return g
            sr = g[len(g) // 2]
            left = [x for x in g if x < sr]
            mid = [x for x in g if x == sr]
            rig = [x for x in g if x > sr]
            return Delivery.vrem(left) + mid + Delivery.vrem(rig)

        def ves_0(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = Delivery.ves_0(arr[:mid])
            right = Delivery.ves_0(arr[mid:])
            return Delivery.ves_1(left, right)
        def ves_1(left, right):
            result = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                   result.append(left[i])
                   i += 1
                else:
                   result.append(right[j])
                   j += 1
            result.extend(left[i:])
            result.extend(right[j:])
            return result

        def nomer_1(t, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and t[left] > t[largest]:
               largest = left

            if right < n and t[right] > t[largest]:
               largest = right
            if largest != i:
               t[i], t[largest] = t[largest], t[i]
               Delivery.nomer_1(t, n, largest)

        def nomer_0(t):
            n = len(t)
            for i in range(n // 2 - 1, -1, -1):
               Delivery.nomer_1(t, n, i)

            for i in range(n - 1, 0, -1):
               t[i], t[0] = t[0], t[i]
               Delivery.nomer_1(t, i, 0)

    def konsol():
        print("1.Показать все доставки и их состояние")
        print("2.Добавить доставку")
        print("3.Удалить доставку")
        print("4.Изменить доставки")
        print("5.Сортировать доставки по весу груза")
        print("6.Сортировать доставки по времени")
        print("7.Упорядочить доставки по номеру")
        print("8.Найти доставку по номеру")
        print("9.Найти доставку по времени")
        print("10.Начало выполниния доставок")
        print("11.Выйти")
        vebor = int(input("Выбери номер задачи которую я должен выполнить:"))
        if vebor == 1:
            Delivery.vse(d)
        elif vebor == 2:
            Delivery.new()
        elif vebor == 3:
            Delivery.udal(d)
        elif vebor == 4:
            Delivery.redak(d)
        elif vebor == 5:
            arr = []
            for i in range(d + 1):
                if globals()[f'var_{i}'] != []:
                    arr.append(globals()[f'var_{i}'][3])
            arr = Delivery.ves_0(arr)
            for i in range(d+1):
                for y in range(d+1):
                      if arr[i] == globals()[f'var_{y}'][3]:
                        print(globals()[f'var_{y}'])
            print('')
        elif vebor == 6:
            g = []
            for i in range(d + 1):
                if globals()[f'var_{i}'] != []:
                    g.append(globals()[f'var_{i}'][4])
            arr = Delivery.vrem(g)
            for i in range(d+1):
                for y in range(d+1):
                    if arr[i] == globals()[f'var_{y}'][4]:
                        print(*globals()[f'var_{y}'])
            print('')
        elif vebor == 7:
            t = []
            for i in range(d + 1):
                if globals()[f'var_{i}'] != []:
                    t.append(globals()[f'var_{i}'][0])
            Delivery.nomer_0(t)
            for i in range(d + 1):
                for y in range(d + 1):
                    if t[i] == globals()[f'var_{y}'][0]:
                        print(*globals()[f'var_{y}'])
            print('')
        elif vebor == 8:
            Delivery.poisk(d)
        elif vebor == 9:
            print('Поиск доставки по времени')
            x = int(input('Введите время доставки которую хотите найти:'))
            arr = []
            for i in range(d + 1):
                if globals()[f'var_{i}'] != []:
                    arr.append(globals()[f'var_{i}'][4])
            f = Delivery.vrem(arr)
            u = []
            for i in range(d + 1):
                for y in range(d + 1):
                    if globals()[f'var_{y}'] != []:
                       if globals()[f'var_{y}'][4] == f[i]:
                          u.append(globals()[f'var_{y}'])
            res = Delivery.poisk_v(f, x)
            if res != -1:
                 print(u[res])
            else:
                 print("Элемент не найден в массиве")
            print("")
        elif vebor == 10:
            Delivery.start(d)
        elif vebor == 11:
            quit()
        else:
            print('')
            konsol()
    konsol()