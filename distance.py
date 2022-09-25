# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример:
# o	A (3,6); B (2,1) -> 5,09
# o	A (7,-5); B (1,-1) -> 7,21


import math


def get_distance(coordinate_points):
    dist = math.hypot(coordinate_points[2] - coordinate_points[0],
                      coordinate_points[3] - coordinate_points[1])
    return dist


def get_coordinates():
    names = ['x1', 'y1', 'x2', 'y2']
    coordinates = []
    for i in range(4):
        crd = float(input(f'Enter the coordinate {names[i]} of the points: '))
        coordinates.append(crd)
    return coordinates


length = get_distance(get_coordinates())
print('The distance between the points: ', length)
