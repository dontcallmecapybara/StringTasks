'''
Задание 9.
Дано предложение. В нем только два слова одинаковые. Найти эти слова.
'''


def find_duplicate_words(text):
    words = text.lower().split()
    duplicates = []
    for word in words:
        if words.count(word) > 1 and word not in duplicates:
            duplicates.append(word)
    return duplicates


text = str(input())
words = text.lower().split()

copies = []
for i in words:
    if words.count(i) == 2 and i not in copies:
        copies.append(i)

print(copies)
