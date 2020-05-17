"""1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
 заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
 алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных"""

import random

array = [random.randint(-100, 99) for _ in range(30)]
print(f'Начальный массив - {array}')


def sort_bubble(array):
    for i in range(len(array) - 1):
        for j in range((len(array) - 1) - i):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    print(f'Отсортированный массив - {array}')


sort_bubble(array)
