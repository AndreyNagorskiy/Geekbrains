""" 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""

import random

array = [random.randint(0, 100) for _ in range(15)]
# array = [2, 4, 5, 1]
# index = 0
max = 0
min = 0

print(f'Начальный массив: {array}')

for item in range(len(array) - 1):
    if array[item] < array[min]:
        min = item
    elif array[item] > array[max]:
        max = item
print('Позиция в массиве считается с 0!')
print(f'Минимальный элемент: позиция - {min}, значение - {array[min]}')
print(f'Максимальный элемент: позиция - {max}, значение - {array[max]}')
swap = array[min]
array[min] = array[max]
array[max] = swap

print(f'Итоговый массив: {array}')