from functools import partial

def net_salary(gross_salary, tax_rate): #++++++++ Чистая зарплата
    return gross_salary-(gross_salary*tax_rate)
def hours_per_day(hours):#++++++++ количество отработаных часов
    def inner(day):
        return day * hours
    return inner
def bonus_percentage(bonus): #++++++++ Бонус вашей зарплаты
    def inner(many):
        return many//100 * bonus
    return inner
def final_salary(base_salary, bonus):#++++++++ Финальная зарплата вместе с бонусом
    return base_salary + bonus
def composed_salary_function(zar,bonus):
    return zar * bonus
def final_salary_composition(gross_salary, bonus): #++++++++Итоговая зарплата после вычетов налогов и добавление бонусов
    return gross_salary+bonus

zar = int(input('Какая у вас зарплата?'))
day=int(input('Сколько дней отработано:'))
h=int(input('Сколько часов в день отработано:'))
ee=int(input('Сколько ценится 1 час:'))

res_bon = bonus_percentage(10)(zar)
print(f'Бонус вашей зарплаты:{res_bon}')

bonus_500 = partial(final_salary, bonus=res_bon )
result = bonus_500(zar)
print(f'Итоговая зарплата без вычетов налогов:{result}')

res_day = hours_per_day(day)(h)
print(f'Количество отработаных часов :{res_day}')

tax_20 = partial(net_salary, tax_rate=0.20)
res_w = tax_20(zar)
print(f'Чистая зарплата:{res_w}')

result = composed_salary_function(res_day, ee)
print(f'Итоговая зарплата по часам:{result}')

result = final_salary_composition(res_w, res_bon)
print(f'Итоговая зарплата после вычетов налогов и добавление бонусов:{result}')