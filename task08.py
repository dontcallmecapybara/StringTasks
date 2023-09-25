'''
Задание 8.
Дано предложение. Напечатать все его слова в порядке неубывания их длин.
'''

text = list(input())

new_text = []
for i in range(len(text)):
    if text[i].isalpha():
        new_text.append(text[i])
    elif text[i] == ' ':
        new_text.append(' ')

text = ''
for j in range(len(new_text)):
    text += new_text[j]

sorted_text = sorted(text.split(), key=lambda word: len(word))
print(sorted_text)
