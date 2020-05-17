# 5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.


number = int(input("Введите номер буквы в алфавите: "))

Alphabet = 'abcdefghijklmnopqrstuvwxyz'

number_alphabet = Alphabet[number - 1]
print(f'Этому номеру соответствует буква {number_alphabet}')