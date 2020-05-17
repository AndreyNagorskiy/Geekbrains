""" 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для
каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно
 вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
 Задача считается решённой, если в ней использована как минимум одна коллекция из модуля collections."""

from collections import namedtuple, OrderedDict

amount = int(input('Введите количество предприятий: '))
b = {}
for company in range(1, amount + 1):
    name = str(input(f'Введите название {company}-ого предприятия: '))
    quarter_1 = int(input(f'Введите прибыль {company}-ого предприятия за 1 квартал: '))
    quarter_2 = int(input(f'Введите прибыль {company}-ого предприятия за 2 квартал: '))
    quarter_3 = int(input(f'Введите прибыль {company}-ого предприятия за 3 квартал: '))
    quarter_4 = int(input(f'Введите прибыль {company}-ого предприятия за 4 квартал: '))
    profit = [quarter_1, quarter_2, quarter_3, quarter_4]
    sum_profit = sum(profit)
    b[name] = sum_profit

info = OrderedDict(sorted(b.items(), key=lambda x: x[1]))
count = 0
summ = 0
for key, value in info.items():
    summ += value
    count += 1
avg_companies = summ / count

for key, value in info.items():
    if value > avg_companies:
        print(f'{key}:{value} - прибыль выше среднего \n')
    elif value < avg_companies:
        print(f'{key}:{value} - прибыль ниже среднего \n')
