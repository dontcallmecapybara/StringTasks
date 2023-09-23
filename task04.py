'''
Задание 4.
Определите какой символ встречается ровно три раза в тексте. Гарантируется, что символ
с такой частотой встречаемости только один.
'''

text_input = str(input())

text_input = text_input.lower()
text = list(text_input)
text.sort()

for i in range(len(text) - 3):
    if text[i] == text[i+1] and text[i] == text[i+2]:
        x = text[i]
    else:
        continue

print(x)
