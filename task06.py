'''
Задание 6.
Дано предложение. Напечатать его в обратном порядке слов.
'''

text = str(input())
text = text.split()
text.reverse()

for i in range(len(text)):
    print(text[i], end=' ')
