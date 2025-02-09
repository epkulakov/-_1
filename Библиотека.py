print("Добро пожаловать в систему управления библиотекой!")
f = open("Библиотека.txt", 'w')
b = []
title= ["Три богатыря", "Война и мир","Бородино","Хамелион","Чудесный Доктор","Я покинул родимый дом","Хорошее отношение к лошедям","Выезд","Русская Природа","Экспонат №..."]
author = ["Пушкин", "Толстой","Лермонтов","Чехов","Куприн","Есенин","Маяковский","Самойлов","Евтушенко","Васильев"]
year = [1856, 1900, 1656, 1458, 1589, 1645, 1689, 1710, 1756, 1500]
for z in range(len(year)):
    b.insert(z, f'{year[z]},"{title[z]}", {author[z]} ')
i = 10
while True:
      def heap(ar, n, p):
        largest = p
        left = 2 * p + 1
        right = 2 * p + 2

        if left < n and ar[left] > ar[largest]:
            largest = left

        if right < n and ar[right] > ar[largest]:
            largest = right

        if largest != p:
            ar[p], ar[largest] = ar[largest], ar[p]
            heap(ar, n, largest)

      def sort_books_by_author(ar):
        n = len(ar)

        for p in range(n // 2 - 1, -1, -1):
            heap(ar, n, p)

        for p in range(n - 1, 0, -1):
            ar[p], ar[0] = ar[0], ar[p]
            heap(ar, p, 0)

      def merge_sort(arr):
        if len(arr) <= 1:
              return arr
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)


      def merge(left, right):
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

      def sort_books_by_year(year):
        if len(year) <= 1:
                return year
        pivot = year[len(year) // 2]
        left = [x for x in year if x < pivot]
        middle = [x for x in year if x == pivot]
        right = [x for x in year if x > pivot]
        return sort_books_by_year(left) + middle + sort_books_by_year(right)
      print("Выберите действие:")
      print("1. Показать все книги")
      print("2. Сортировать книги по названию")
      print("3. Сортировать книги по автору")
      print("4. Сортировать книги по году издания")
      print("5. Найти книгу по названию")
      print("6. Найти книгу по автору")
      print("7. Добавить книгу")
      print("8. Удалить книгу")
      print("9. Выйти")
      v = int(input("Введите номер действия:"))
      if v == 1:
          k = 0
          for f in range(len(b)):
              print(*b[k])
              k += 1

      elif v == 2:
         arr = []
         for s in range(len(title)):
             arr.insert(s,len(title[s]))
         ert = merge_sort(arr)
         for t in range(len(title)):
             for y in range(len(title)):
                 if ert[t] == len(title[y]):
                     print(title[y],'  ' ,author[y], year[y])
         print(ert)

      elif v == 3:
          ar = []
          for s1 in range(len(author)):
              ar.insert(s1, len(author[s1]))
          sort_books_by_author(ar)
          y = ar
          for t in range(len(title)):
              for j in range(len(author)):
                  if y[t] == len(author[j]):
                      print(author[j],title[j], year[j])
                      break
          print(y)

      elif v == 4:
         sort_books_by_year(year)
         er = sort_books_by_year(year)
         for t in range(len(title)):
             for y in range(len(title)):
                 if er[t] == year[y]:
                     print (er[t], author[y], title[y])
         print(er)

      elif v == 5:
         q = input('Напишите нзвание книги которую хотите найти')
         for c in range(len(b)):
             if title[c] == q:
                 print(b[c])
                 break

      elif v == 6:
          q = input('Напишите Автора книги которую хотите найти')
          for c in range(len(b)):
              if author[c] == q:
                  print(b[c])

      elif v == 7:
          print('Добавлениее новой книги')
          title.insert(i, input('Название книги'))
          author.insert(i, input('Автор книги'))
          year.insert(i, int(input('Год книги')))
          r = (f'{year[i]},"{title[i]}", {author[i]} ')
          b.insert(i ,r)
          print(*b, sep=' ')
          i += 1

      elif v == 8:
          for x in range(len(b)):
              print(x,'.  ', *b[x], sep=' ')
          c = int(input("Выбирите номер книги которую хотите удалить"))
          del b[c]

      elif v == 9:
        f.write(f'{title} \n {author} \n  {b}')
        f.close()
        quit()