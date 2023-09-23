'''
Задание 5.
Даны три строки. Выведите на экран только те символы, которые есть лишь в одной из этих трёх строк.
'''

text_input1 = str(input())
text_input2 = str(input())
text_input3 = str(input())

text_input1 = text_input1.lower()
text1 = list(text_input1)
text1.sort()

text_input2 = text_input2.lower()
text2 = list(text_input2)
text2.sort()

text_input3 = text_input3.lower()
text3 = list(text_input3)
text3.sort()

word_list = []

for i in range(len(text1)):
    if text1[i] not in text2 and text1[i] not in text3:
        word_list.append(text1[i])

for j in range(len(text2)):
    if text2[j] not in text1 and text2[j] not in text3:
        word_list.append(text2[j])

for f in range(len(text3)):
    if text3[f] not in text1 and text3[f] not in text2:
        word_list.append(text3[f])

word_list = list(set(word_list))
word_list.sort()

for h in range(len(word_list)):
    print(word_list[h], end='  ')
