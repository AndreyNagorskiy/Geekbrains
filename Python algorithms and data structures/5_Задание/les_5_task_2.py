"""2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
 При этом каждое число представляется как массив, элементы которого — цифры числа.

Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
 Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

 Задача считается решённой, если в ней использована как минимум одна коллекция из модуля collections."""

from collections import deque
print('Вводите числа без дробной части \n')
number_1 = deque((str(input(f'Введите первое число: '))))
number_2 = deque((str(input(f'Введите второе число: '))))

dict = {
    '0': '0',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    'A': '10',
    'B': '11',
    'C': '12',
    'D': '13',
    'E': '14',
    'F': '15',
    '16': '10'
}


def to_base_10(num):
    result = []
    index = 0
    for key, value in dict.items():
        if index < len(num):
            numeral = num[index]
            num_10 = dict[numeral]
            result.append(num_10)
            index += 1

    length = len(result) - 1

    i = 0
    list_10 = []
    while i < len(result):
        num = int(result[i]) * (16 ** length)
        length -= 1
        i += 1
        list_10.append(num)

    base_10 = sum(list_10)
    return base_10


base_10_num_1 = to_base_10(number_1)
base_10_num_2 = to_base_10(number_2)
summ = base_10_num_1 + base_10_num_2
mul = base_10_num_1 * base_10_num_2


def base_to_16(num):
    base = 16
    base_to_16.t = '0123456789ABCDEF'
    r = ''
    while num:
        num, y = divmod(num, base)
        r = base_to_16.t[y] + r
    return r


result_sum = deque(base_to_16(summ))
result_mul = deque(base_to_16(mul))

print(f'Сумма чисел равна : {list(result_sum)}')
print(f'Произведение чисел равна : {list(result_mul)}')
