"""1. Проанализировать скорость и сложность одного любого алгоритма из разработанных
в рамках домашнего задания первых трех уроков. """
from collections import Counter
import random
import cProfile


# Определить, какое число в массиве встречается чаще всего.
def Frequency(x):
    array = [random.randint(0, 10) for _ in range(x)]
    data = Counter(array)
    return data.most_common(1)[0][0]


# "task_1_variant_2.Frequency(100)"
# # 1000 loops, best of 5: 322 usec per loop
#
# # "task_1_variant_2.Frequency(500)"
# # 1000 loops, best of 5: 1.55 msec per loop
#
# # "task_1_variant_2.Frequency(1000)"
# # 1000 loops, best of 5: 3.11 msec per loop
#
# # cProfile.run('Frequency(100)')
# # 579 function calls (571 primitive calls) in 0.001 seconds
#
# # cProfile.run('Frequency(500)')
# # 2729 function calls (2721 primitive calls) in 0.002 seconds
#
# # cProfile.run('Frequency(1000)')
# # 5483 function calls (5475 primitive calls) in 0.005 seconds

"""Получается, что 2 вариант является самым лучшим, поскольку он производительнее остальных вариантов."""

print((Frequency(100)))
