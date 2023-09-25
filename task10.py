'''
Задание 10.
Дано предложение. Выведите на экран те слова, которые отличны от первого слова
и в слове нет повторяющихся букв.
'''

text = list(input().lower())

new_text = []
for i in range(len(text)):
    if text[i].isalpha():
        new_text.append(text[i])
    elif text[i] == ' ':
        new_text.append(' ')

text = ''
for j in range(len(new_text)):
    text += new_text[j]
text = text.split()

first_word = text[0]
del text[0]
for duplicate_word in range(len(text)-1):
    if text[duplicate_word] == first_word:
        del text[duplicate_word]
    else:
        pass

finding_words = []
for word in range(len(text)):
    temp_list = list(text[word])
    unique_words = set(temp_list)
    if len(temp_list) == len(unique_words):
        finding_words.append(text[word])

print(finding_words)
