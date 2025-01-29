class Employee:
   def shell_sort(ar):
     n = len(ar)
     ser = n // 2

     while ser > 0:
         for i in range(ser, n):
             temp = ar[i]
             j = i
             while j >= ser and ar[j - ser] > ar[j]:
                 ar[j] = ar[j - ser]
                 j -= ser
             ar[j] = temp
         ser //= 2

     return ar

name = ['Петров','Кулаков','Карпенко','Бокова','Хаймулина']
cl = Employee
age = cl.shell_sort([20, 19, 18, 25, 21])
many = cl.shell_sort([200000, 210000, 180000, 190000, 220000])
name.sort()
print(f"Фамилии сотрудников по Алфавиту {name}")
print(f'Возрaст : {age}')
print(f'Самый старший : {age[-1]}')
print(f'Самый младший : {age[0]}')

print(f'Заработок : {many}')
print(f'Самый большой зарабаток : {many[-1]}')
print(f'Самый маленький зарабаток : {many[0]}')