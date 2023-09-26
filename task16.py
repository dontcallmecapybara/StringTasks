'''
Задание 16.
Дан текст. Проверить, правильно ли в нем расставлены круглые скобки (т. е.
находится ли справа от каждой открывающей скобки соответствующая ей закрывающая
скобка, а слева от каждой закрывающей — соответствующаяей закрывающая).
'''

counter = 0
text = list(input('Введите текст: '))
result = None
text_copy = str(text)

if text_copy.find('(') == -1 and text_copy.find(')') == -1:
    print('В тексте нет скобок.')
else:
    for symbol in range(len(text)):
        if text[symbol] == ')' and counter <= 0:
            result = 'Скобки расставлены неправильно!'
            break
        elif text[symbol] == '(':
            counter += 1
        elif text[symbol] == ')' and counter > 0:
            counter -= 1
        else:
            pass

    if result is not None:
        print(result)
    elif counter == 0:
        print('Скобки расставлены правильно!')
    else:
        print('Скобки расставлены неправильно!')
