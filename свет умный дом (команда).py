def komanda_vkl():
    global posled
    posled = 1
    print("Свет включён")

def komanda_vk():
    global posled
    posled = 0
    print("Свет выключен")
posled = 0
while True:
    print("Выключить свет нажмите 1,Включить 2,последнее действие 3")
    x = int(input("Если хотите выйти нажмите любую цифру:"))
    if x == 1:
       komanda_vk()
    elif x ==2:
        komanda_vkl()
    elif x == 3:
        if posled == 1:
            print("Свет включён")
        elif posled == 0:
            print("Свет выключен")
    else:
        quit()