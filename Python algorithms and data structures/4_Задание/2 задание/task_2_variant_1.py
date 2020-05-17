"""2. Написать два алгоритма нахождения i-го по счёту простого числа.
 Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
  Проанализировать скорость и сложность алгоритмов."""

"""Первый — с помощью алгоритма «Решето Эратосфена»."""


import functools
import cProfile

@functools.lru_cache()
def sieve(x):
    n = x * 10
    resheto = [i for i in range(n)]
    resheto[1] = 0

    for i in range(2, n):
        if resheto[i] != 0:
            j = i * 2
            while j < n:
                resheto[j] = 0
                j += i

    result = [i for i in resheto if i != 0]
    print(result[x - 1])

sieve(10)
# "task_2_variant_1.sieve(100)"
# 1000 loops, best of 5: 237 nsec per loop

# "task_2_variant_1.sieve(500)"
# 1000 loops, best of 5: 236 nsec per loop

# "task_2_variant_1.sieve(1000)"
# 1000 loops, best of 5: 236 nsec per loop

# cProfile.run('sieve(100)')
# 6 function calls in 0.001 seconds

# cProfile.run('sieve(500)')
# 6 function calls in 0.005 seconds

# cProfile.run('sieve(1000)')
# 6 function calls in 0.011 seconds

"""Получается, оба алгоритма почти идентичны, но алгоритм без Решета немного быстрее.
 Такие одинаковые значения получаются из-за того, что в обоих случаях был использован декоратор для мемоизации."""