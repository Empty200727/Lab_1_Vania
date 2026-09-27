# Задание 01. Круг.
# Круг с центром (0, 0) и радиусом 42. Вывести площадь (4 знака после запятой,
# пи = 3.1415926) и для двух точек определить, лежат ли они в круге.

import math

TITLE = 'Площадь круга и точки'

PI = 3.1415926
radius = 42

point_1 = (23, 34)
point_2 = (30, 30)


def get_area(r):
    return round(PI * r ** 2, 4)


def distance_from_center(x, y):
    return math.sqrt(x ** 2 + y ** 2)


def inside(point, r=radius):
    return distance_from_center(*point) <= r


def run():
    print('Площадь круга:', get_area(radius))
    print('Точка', point_1, '->', inside(point_1))
    print('Точка', point_2, '->', inside(point_2))


if __name__ == '__main__':
    run()
