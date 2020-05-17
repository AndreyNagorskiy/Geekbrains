"""2. Написать два алгоритма нахождения i-го по счёту простого числа.
 Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
  Проанализировать скорость и сложность алгоритмов."""

"""Второй — без использования «Решета Эратосфена»."""

import functools
import cProfile

@functools.lru_cache()
def prime(x):
    n = x * 10
    list = [2]
    for i in range(3, n + 1, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in list:
            if j * j - 1 > i:
                list.append(i)
            break
        if (i % j == 0):
            break
        else:
            list.append(i)
    #print(list[x - 1])

#python -m timeit -n 1000 -s "import task_2_variant_2" "task_2_variant_2.prime(50)"


# "task_2_variant_2.prime(100)"
# 1000 loops, best of 5: 236 nsec per loop

# "task_2_variant_2.prime(500)"
# 1000 loops, best of 5: 239 nsec per loop

# "task_2_variant_2.prime(1000)"
# 1000 loops, best of 5: 236 nsec per loop

# cProfile.run('prime(100)')
#  404 function calls in 0.001 seconds

# cProfile.run('prime(500)')
# 2004 function calls in 0.002 seconds

# cProfile.run('prime(1000)')
# 4004 function calls in 0.005 seconds

"""Получается, оба алгоритма почти идентичны, но алгоритм без Решета немного быстрее.
 Такие одинаковые значения получаются из-за того, что в обоих случаях был использован декоратор для мемоизации."""
