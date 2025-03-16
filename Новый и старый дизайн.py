class Menu():
    def glav(self):
        return "Главная"
    def pod(self):
        return"Поддержка"
    def kat(swlf):
        return "Каталог"
def OldService():                         #Создание def старого интерфейса
    print("Старый интерфейс")             #
    m = Menu()
    print(m.glav(),m.pod(),m.kat())
def NewService():                         #Создание def нового интерфейса
    print("Новый интерфейс")              #
    m = Menu()
    print(m.glav(),"|", m.pod(),"|", m.kat())
class ServiceAdapter():                   #Адаптер для интерфейсов
    def new():
        NewService()
    def star():
        OldService()
ServiceAdapter.new()
while True:
     status = int(input("Если хотите изминить интерфейс нажмите 1-Новый , 2 - старый, 3 - покинуть интерфейс:"))
     if status == 1:
         ServiceAdapter.new()
     elif status == 2:
         ServiceAdapter.star()
     else:
         break