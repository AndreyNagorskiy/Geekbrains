"""1. Проанализировать скорость и сложность одного любого алгоритма из разработанных
в рамках домашнего задания первых трех уроков. """


import random
import cProfile

#Определить, какое число в массиве встречается чаще всего.
def Frequency(x):
    array = [random.randint(0, 10) for _ in range(x)]
    number = max(array, key=array.count)
    return number

# "task_1_variant_3.Frequency(100)"
# 1000 loops, best of 5: 534 usec per loop

# "task_1_variant_3.Frequency(500)"
# 1000 loops, best of 5: 8.05 msec per loop

# "task_1_variant_3.Frequency(1000)"
# 1000 loops, best of 5: 27.9 msec per loop


# cProfile.run('Frequency(100)')
# 564 function calls in 0.001 seconds

# cProfile.run('Frequency(500)')
# 2746 function calls in 0.007 seconds

# cProfile.run('Frequency(1000)')
# 5527 function calls in 0.032 seconds

"""Получается, что 2 вариант является самым лучшим, поскольку он производительнее остальных вариантов."""