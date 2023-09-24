'''
Задание 7.
Дано предложение. Найти длину его самого короткого слова.
'''

text = str(input())
text = text.split()

letter_count = []
for i in range(len(text)):
    if text[i].isalpha():
        letter_count.append(len(text[i]))
    else:
        letter_count.append(len(text[i])-1)

print(min(letter_count))
