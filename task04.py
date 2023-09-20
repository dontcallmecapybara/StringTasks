'''
Задание 4.
Определите какой символ встречается ровно три раза в тексте. Гарантируется, что символ
с такой частотой встречаемости только один.
'''

text_input = str(input())

text_input = text_input.lower()
text = list(text_input)

x = 0
for i in range(len(text)-1):
    if text[i] == text[i+1]:
        x += 1
    elif x == 3:
        word = text[i]
        break
    else:
        x = 0

print(text[i])
