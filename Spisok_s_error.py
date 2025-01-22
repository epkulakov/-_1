def poisk(arr, x):
    left, rig = 0, len(arr) - 1
    while left <= rig:
        m = (left + rig) // 2
        if arr[m] != None:
            if arr[m] == x:
                return m
            elif arr[m] < x:
                left = left + 1
            else:
                rig = m - 1
        elif left > 0:
            left = left  + 1
        elif left < rig:
            rig = m - 1
        else :
            rig = m - 1
    return -1
x = int(input('Какое число надо попробывать найти в списке?'))
arr = [1, 2, None, None, 5, None, 7, None, 10, 11]
print(arr)

res = poisk(arr, x)
if res == -1:
    print("Элемент не найден в массиве (-1)")
else:
    print(f"Элемент найден на индексе {res}")