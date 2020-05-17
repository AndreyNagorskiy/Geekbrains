# 4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят,
# и сколько между ними находится букв.

print("Введите 2 символа:")
a = str(input("Введите первый символ = "))
b = str(input("Введите второй символ = "))

Alphabet = 'abcdefghijklmnopqrstuvwxyz'

index_a = Alphabet.find(a) + 1
index_b = Alphabet.find(b) + 1

if index_a > index_b:
    between = index_a - index_b - 1
else:
    between = index_b - index_a - 1

print(f'Буква {a} находится на {index_a} месте алфавита')
print(f'Буква {b} находится на {index_b} месте алфавита')
print(f'Букв между ними: {between}')
