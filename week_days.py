# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# o	6 -> да
# o	7 -> да
# o	1 -> нет

def is_day_off():
    number = int(input('Enter integer number from 1 to 7: '))
  
    if number in (6, 7):
        print('It`s a day off')
    elif 1 <= number < 6:
        print('It`s NOT a day off')
    else:
        print('bad number')


is_day_off()
