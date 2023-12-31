'''
Задание 15.
Напишите программу, позволяющую организовать игру "Быки и коровы" с десятью попытками
отгадать число. Программа должна спрашивать у ведущего четырехзначное целое число с
неповторяющимися цифрами. Далее, программа удаляет информацию с экрана, выполняя
вывод 25 пустых строк. После этого, игрок пытается отгадать загаданное число.
После каждой попытки, программа сообщает количество "быков" и "коров". Быки - цифры
совпавшие с загаданным числом и при этом находящиеся на тех же позициях. Коровы - цифры,
которые есть в загаданном числе, но находятся на других позициях. В случае если число
отгадано верно, выводится сообщение "Победа!". Если закончились попытки, выводится
сообщение "Проигрыш!".

Пример работы программы:
Ведущий вводит число.
9305
Программа выводит 25 пустых строк и таким образом "скрывает" то, что написал ведущий.
Игрок пытается отгадать число:
1234
Быков: 0 Коров: 1
5678
Быков: 0 Коров: 1
9012
Быков: 1 Коров: 1
9087
Быков: 1 Коров: 1
1087
Быков: 0 Коров: 1
9205
Быков: 3 Коров: 0
9305
Быков: 4 Коров: 0
Победа
'''

def game():
    attempts = 0
    while True:
        number = input('Введите ваш вариант: ')
        if not number.isdigit() and len(number) == 4:
            print('Введите четырехзначное число.')

        male_cow, female_cow = how_much(answer, number)
        attempts += 1

        if male_cow == 4:
            print(f'Поздравляем! Вы угадали число {answer} за {attempts} попыток.')
            break
        else:
            print(f'Быки: {male_cow}, Коровы: {female_cow}')

def how_much(answer, number):
    male_cow = female_cow = 0
    for i in range(4):
        if number[i] == answer[i]:
            male_cow += 1
        elif number[i] in answer:
            female_cow += 1
    return male_cow, female_cow


answer = input('Загадайте четырехзначное число: ')
if len(answer) != 4 or answer.isdigit() == False:
    print('Вы ввели не четырехзначное число.')
else:
    print('\n' * 25)
    game()
