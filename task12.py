'''
Задание 12.
Как известно, имя в языке Python может содержать только латинские символы, цифры
и знак подчеркивания "_". При этом, имя не может начинаться с цифры и не может быть
ключевым словом. Напишите программу, которая проверяет введенную строку, может ли
она быть именем в языке Python.
'''

import keyword

name = input()

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
special = "_"
characters = list(upper + lower + numbers + special)

valid_name = True

if keyword.iskeyword(name):
    valid_name = False
else:
    name = list(name)
    if name[0] in numbers:
        valid_name = False
    else:
        for i in list(name):
            if i not in characters:
                valid_name = False
                break

if valid_name:
    print('The string can be a name.')
else:
    print('The string cannot be a name.')
