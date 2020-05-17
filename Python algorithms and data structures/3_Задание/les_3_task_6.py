""" 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
 Сами минимальный и максимальный элементы в сумму не включать."""

import random

array = [random.randint(1, 150) for _ in range(15)]
print(f'Начальный массив: {array}')

min = 0
max = 0
sum = 0

for item in range(1, len(array)):
    if array[item] < array[min]:
        min = item
    elif array[item] > array[max]:
        max = item
print(f'Минимальное значение: {array[min]}, максимальное значение: {array[max]}')

if min > max:
    min =  max
    max = min

for item in range(min + 1, max):
    sum += array[item]
print(f'Сумма элементов между ними: {sum}')

