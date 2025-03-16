class Menu(): #Cоздание класа для объектов
    def glav(self):#объект главная
        return "Главная"#возращаем
    def pod(self):#объект поддержка
        return"Поддержка"#возращаем
    def kat(swlf):#объект каталог
        return "Каталог"#возращаем
def OldService():                         #Создание def старого интерфейса
    print("Старый интерфейс")             #Выводим название интерфейса в котором мы сейчас
    m = Menu()
    print(m.glav(),m.pod(),m.kat())      #вывод самого меню
def NewService():                         #Создание def нового интерфейса
    print("Новый интерфейс")              #Выводим название интерфейса в котором мы сейчас
    m = Menu()
    print(m.glav(),"|", m.pod(),"|", m.kat())#вывод самого меню
class ServiceAdapter():                   #Адаптер для интерфейсов
    def new():
        NewService()
    def star():
        OldService()
ServiceAdapter.new()
while True:#делаем вечный цикл для обработки постояных запросов
     status = int(input("Если хотите изминить интерфейс нажмите 1-Новый , 2 - старый, 3 - покинуть интерфейс:"))
     if status == 1:
         ServiceAdapter.new() #вызываем определённый метод в зависимости от выбора
     elif status == 2:
         ServiceAdapter.star()#вызываем определённый метод в зависимости от выбора
     else:
         break  #для выхода из програмы
