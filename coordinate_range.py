# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).


def xy_range(number_quarter):
    if number_quarter == 1:
        print('Range: X>0 and Y>0')
    elif number_quarter == 2:
        print('Range: X<0 and Y>0')
    elif number_quarter == 3:
        print('Range: X<0 and Y<0')
    elif number_quarter == 4:
        print('Range: X>0 and Y<0')


quarter = int(input('Enter number of quarter: '))
xy_range(quarter)
