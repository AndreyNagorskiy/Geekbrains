"""1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в
 рамках первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным
  использованием памяти."""
import sys
import random


def show_size(var1, var2, var3):
    summ = sys.getsizeof(var1) + sys.getsizeof(var2) + sys.getsizeof(var3)
    print(f'Размер занимаемой памяти всех переменных: {summ} байт(-а)')


def Frequency(x):
    array = [random.randint(0, 10) for _ in range(x)]
    result = []
    max = 1
    for item in range(len(array)):
        result.append(array.count(array[item]))
    for item in range(len(result)):
        if result[item] > result[max]:
            max = item
    show_size(x, array, result)
    # return array[max]

print(f'Версия системы - {sys.version}')
print(f'Платформа - {sys.platform}')
Frequency(100)

# Версия системы - 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)]
# Платформа - win32
# Размер занимаемой памяти всех переменных: 934 байт


""" Получается, что самым лучшим вариантом с точки зрения занимаемой памяти является 3 вариант, поскольку
он занимает наименьшее место в памяти (486 байт). Это происходит из-за того, что в 1 и 2 варианте присутствует два
списка, которые занимают больше места, в 3 же варианте вместо 2-ого списка есть переменная, содержащая лишь одно число."""