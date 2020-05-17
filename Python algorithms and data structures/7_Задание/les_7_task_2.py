""" 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
 на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы."""

import random

array = [random.randint(0, 49) for _ in range(15)]
print(f'Начальный массив - {array}')

def merge(left_array, right_array):
    sorted_list = []
    left_array_index = right_array_index = 0
    left_array_length, right_array_length = len(left_array), len(right_array)

    for _ in range(left_array_length + right_array_length):
        if left_array_index < left_array_length and right_array_index < right_array_length:
            if left_array[left_array_index] <= right_array[right_array_index]:
                sorted_list.append(left_array[left_array_index])
                left_array_index += 1
            else:
                sorted_list.append(right_array[right_array_index])
                right_array_index += 1
        elif left_array_index == left_array_length:
            sorted_list.append(right_array[right_array_index])
            right_array_index += 1
        elif right_array_index == right_array_length:
            sorted_list.append(left_array[left_array_index])
            left_array_index += 1

    return sorted_list

def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left_array = merge_sort(nums[:mid])
    right_array = merge_sort(nums[mid:])
    return merge(left_array, right_array)
#
print(f'Отсортированный массив - {merge_sort(array)}')


