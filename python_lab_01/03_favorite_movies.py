# Задание 03. Любимые фильмы.
# Только срезами (без split/find) вывести первый, последний, второй
# и второй с конца фильм. Строку менять нельзя, запятые не выводить.

TITLE = 'Срезы строки с фильмами'

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'


def cut_titles(movies):
    # Все пять названий по порядку, границы подсчитаны по символам
    return [
        movies[0:10],
        movies[12:25],
        movies[27:33],
        movies[35:40],
        movies[42:],
    ]


def get_answer(movies):
    titles = cut_titles(movies)
    return [titles[0], titles[-1], titles[1], titles[-2]]


def run():
    for number, title in enumerate(get_answer(my_favorite_movies), start=1):
        print(f'{number}) {title}')


if __name__ == '__main__':
    run()
