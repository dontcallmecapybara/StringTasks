'''
Задание 2.
Дан текст. Необходимо определить максимальное количество последовательных одинаковых символов в нём.
'''

text_input = str(input())

text_input = text_input.lower()
text = list(text_input)

x = 1
y = 0

for i in range(len(text_input) - 1):
    if text[i+1] == text[i]:
        x += 1
    else:
        if y < x:
            y = x
        x = 1

print(y)
