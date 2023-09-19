'''
Задание 3.
Дан текст. Определить, сколько различных букв в нем.
'''

text_input = str(input())

text_input = text_input.lower()
text_almost_ready = list(text_input)

text = []
for i in range(len(text_almost_ready)):
    if text_almost_ready[i].isalpha():
        text.append(text_almost_ready[i])

a = []
for j in range(len(text)):
    if text[j] not in a:
        a.append(text[j])

print(len(a))
