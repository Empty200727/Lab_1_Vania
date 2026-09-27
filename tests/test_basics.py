# Тесты заданий 00-04
from pytest import approx

from helpers import get

distance = get('00_distance')
circle = get('01_circle')
operations = get('02_operations')
movies = get('03_favorite_movies')
family = get('04_my_family')


def test_distance_simple_triangle():
    result = distance.get_distances({'A': (0, 0), 'B': (0, 5), 'C': (12, 0)})
    assert result['A'] == {'B': 5, 'C': 12}
    assert result['B']['C'] == 13


def test_distance_cities():
    result = distance.get_distances(distance.sites)
    assert result['Moscow']['Paris'] == approx(130.384)
    assert result['Moscow']['Paris'] == result['Paris']['Moscow']


def test_circle_area():
    assert circle.get_area(42) == 5541.7693


def test_points():
    assert circle.inside(circle.point_1)
    assert not circle.inside(circle.point_2)
    assert circle.inside((0, -42))


def test_operations():
    assert operations.example() == 9
    assert operations.answer() == 25
    assert eval(operations.ANSWER) == 25


def test_movies():
    assert movies.cut_titles(movies.my_favorite_movies)[2] == 'Аватар'
    assert movies.get_answer(movies.my_favorite_movies) == [
        'Терминатор', 'Назад в будущее', 'Пятый элемент', 'Чужие',
    ]


def test_family():
    assert family.father_height(family.my_family, family.my_family_height) == 181
    assert family.sum_height(family.my_family_height) == 846
    assert len(family.my_family_height) == len(family.my_family)
