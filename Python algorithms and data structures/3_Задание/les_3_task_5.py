""" В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
 Это два абсолютно разных значения."""

import random

array = [random.randint(-100, -1) for _ in range(15)]
print(f'Начальный массив: {array}')
print('Позиция в массиве считается с 0!')
i = 0
index = -1
while i < (len(array)):
    if array[i] < 0 and index == -1:
        index = i
    elif array[i] < 0 and array[i] > array[index]:
        index = i
    i += 1

print(f'Позиция в массиве: {index}, Значение: {array[index]}')