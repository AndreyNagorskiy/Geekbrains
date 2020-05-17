"""3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
 в другой — не больше медианы."""

import statistics
import random

rng = 2 * 6 + 1
array = [random.randint(0, 99) for _ in range(rng)]
print(f'Исходный массив: {array}')
# 1 вариант
print(f'Первый вариант нахождения: {statistics.median(array)}')


# 2 вариант
def find_median(array):
    array = sorted(array)
    if len(array) % 2 == 1:
        return array[int(len(array) / 2)]
    else:
        return 0.5 * (array[int(len(array) / 2 - 1)] + array[int(len(array) / 2)])


print(f'Второй вариант нахождения: {find_median(array)}')
