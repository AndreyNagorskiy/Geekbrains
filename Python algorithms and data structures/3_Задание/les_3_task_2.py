""" 2. Во втором массиве сохранить индексы четных элементов первого массива.
 Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5
(помните, что индексация начинается с нуля), т. к. именно в этих позициях первого массива стоят четные числа."""
import random

first_array = [random.randint(0, 50) for _ in range(15)]
second_array = []

for index, item in enumerate(first_array):
    if item % 2 == 0:
        second_array.append(index)

print(f'Первый массив - {first_array}')
print(f'Второй массив - {second_array}')
