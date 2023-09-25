'''
Задание 9.
Дано предложение. В нем только два слова одинаковые. Найти эти слова.
'''

text = list(input().lower())
unique_words = set()

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

for f in text:
    unique_words.add(f)

duplicate_words = []
for word in unique_words:
    if text.count(word) == 2:
        duplicate_words.append(word)

print('Word is ' + '"' + duplicate_words[0] + '".')
