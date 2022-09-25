# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# o	x=34; y=-30 -> 4
# o	x=2; y=4-> 1
# o	x=-34; y=-30 -> 3


def what_quarter(a, b):
    if a > 0 and b > 0:
        print('1st quarter')
    elif a < 0 and b > 0:
        print('2nd quarter')
    elif a < 0 and b < 0:
        print('3d quarter')
    elif a > 0 and b < 0:
        print('4th quarter')
    elif a == 0 and b != 0:
        print('This is an Axis Y')
    elif b == 0 and a != 0:
        print('This is an Axis X')
    elif a == 0 and b == 0:
        print('This is the center of coordinate')


x = float(input('Enter number X: '))
y = float(input('Enter number Y: '))   

what_quarter(x, y)

