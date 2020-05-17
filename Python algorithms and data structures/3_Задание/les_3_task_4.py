""" 4. Определить, какое число в массиве встречается чаще всего."""

import random


def Frequency(x):

    array = [random.randint(0, 10) for _ in range(x)]
    result = []
    max = 1
    print(f'Начальный массив: {array}')
    for item in range(len(array)):
        result.append(array.count(array[item]))
    for item in range(len(result)):
        if result[item] > result[max]:
            max = item

    print(f'Число {array[max]} встречается {result[max]} раз(а)')

Frequency(100)
