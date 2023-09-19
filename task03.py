'''
Задание 3.
Дан текст. Определить, сколько различных букв в нем.
'''

text_input = str(input())

text_input = text_input.lower()
text = list(text_input)
a = []

for i in range(len(text)):
    if text[i] not in a:
        a.append(text[i])

print(len(a))
