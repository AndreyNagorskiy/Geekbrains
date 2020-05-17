# 3. Написать программу, которая генерирует в указанных пользователем границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить
# случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
import random

print("Границы для целых чисел:")
int_start_border = int(input("Введите начало границы = "))
int_end_border = int(input("Введите конец границы  = "))

print("Границы для вещественных чисел:")
float_start_border = float(input("Введите начало границы = "))
float_end_border = float(input("Введите конец границы = "))

print("Границы для символов:")
chr_start_border = str(input("Введите начало границы = "))
chr_end_border = str(input("Введите конец границы = "))

random_int = random.randint(int_start_border, int_end_border)
random_float = random.uniform(float_start_border, float_end_border)
Alphabet = 'abcdefghijklmnopqrstuvwxyz'
random_chr = Alphabet[random.randint(Alphabet.find(chr_start_border), Alphabet.find(chr_end_border))]

print(f'Случайное целое число: {random_int}')
print(f'Cлучайное вещественное число: {random_float}')
print(f'Cлучайный символ: {random_chr}')
