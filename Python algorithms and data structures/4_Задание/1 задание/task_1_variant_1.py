"""1. Проанализировать скорость и сложность одного любого алгоритма из разработанных
в рамках домашнего задания первых трех уроков. """
import random
import cProfile

#Определить, какое число в массиве встречается чаще всего.

def Frequency(x):
    array = [random.randint(0, 10) for _ in range(x)]
    result = []
    max = 1
    for item in range(len(array)):
        result.append(array.count(array[item]))
    for item in range(len(result)):
        if result[item] > result[max]:
            max = item
    return array[max]

# "task_1_variant_1.Frequency(100)"
# 1000 loops, best of 5: 587 usec per loop

# "task_1_variant_1.Frequency(500)"
# 1000 loops, best of 5: 7.84 msec per loop

# "task_1_variant_1.Frequency(1000)"
# 1000 loops, best of 5: 26.9 msec per loop

# cProfile.run('Frequency(100)')
# 745 function calls in 0.001 seconds

# cProfile.run('Frequency(500)')
# 3719 function calls in 0.009 seconds

# cProfile.run('Frequency(1000)')
# 7409 function calls in 0.031 seconds

"""Получается, что 2 вариант является самым лучшим, поскольку он производительнее остальных вариантов."""