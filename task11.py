'''
Задание 11.
Петя и Вася играют в игру "Города". Первым называет город Петя. Каждый следующий,
называемый город должен начинаться на ту букву, на которую окончился предыдущий.
Программа получает на вход строку, состоящую из слов (городов), разделенных пробелами,
которые называли игроки. В результате работы, программа должна определять имя победителя.
Игрок выигрывает, если он назвал слово последним. Однако, игрок проигрывает, если он
первым нарушил правила игры.
'''


text = list(map(str, input().lower()))

except_letter = ['ь', 'ъ']
words = ''
for letter in range(len(text)):
    if text[letter].isalpha() and text[letter] not in except_letter:
        words += text[letter]
    elif text[letter] == ' ':
        words += ' '

counter = 1
words = list(words)
for i in range(len(words)-2):
    if words[i].isalpha() and words[i+1] == ' ' and words[i+2].isalpha():
        if words[i] == words[i+2]:
            counter += 1
        else:
            pass
    else:
         pass

if counter % 2 == 0:
    print('Winner is Vasya')
else:
    print('Winner is Petya')
