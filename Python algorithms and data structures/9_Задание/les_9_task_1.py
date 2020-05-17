"""1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке."""

import hashlib


def number_of_substrings(string):
    substring = set()
    for i in range(len(string) + 1):
        for j in range(i + 1, len(string) + 1):
            h = hashlib.sha1(string[i:j].encode('utf-8')).hexdigest()
            substring.add(h)

    return len(substring)


string = input('Введите строку: ')
print(f'Количество различных подстрок в строке "{string}" - {number_of_substrings(string)} подстрок')
