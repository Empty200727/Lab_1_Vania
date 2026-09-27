# Задание 00. Расстояния между городами.
# По координатам городов составить словарь словарей расстояний:
# distances['Moscow']['London'] -> расстояние между Москвой и Лондоном.

import math

TITLE = 'Расстояния между городами'

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}


def get_distance(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return math.sqrt(dx ** 2 + dy ** 2)


def get_distances(points):
    distances = dict()
    for town, coords in points.items():
        distances[town] = dict()
        for other_town, other_coords in points.items():
            if other_town != town:
                distances[town][other_town] = round(get_distance(coords, other_coords), 3)
    return distances


def run():
    result = get_distances(sites)
    for town in result:
        print(town, result[town])


if __name__ == '__main__':
    run()
