""" 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
 Например, если введено число 3486, надо вывести 6843."""

num = int(input('Введите целое число:'))

n2 = 0

while num > 0:
    remainder = num % 10
    num = num // 10
    n2 = n2 * 10
    n2 += remainder

print(f'Обратное ему число: {n2}')
