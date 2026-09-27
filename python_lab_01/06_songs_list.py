# Задание 06. Песни Depeche Mode (альбом Violator).
# 1) по списку: 'Halo', 'Enjoy the Silence', 'Clean';
# 2) по словарю: 'Sweetest Perfection', 'Policy of Truth', 'Blue Dress'.
# Результат округлить до 3 знаков после запятой.

TITLE = 'Длительность песен'

violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}


def total_time(songs, names):
    # Список пар легко превращается в словарь, дальше код общий
    if isinstance(songs, list):
        songs = dict(songs)
    result = 0.0
    for name in names:
        result += songs[name]
    return round(result, 3)


def run():
    first = total_time(violator_songs_list, ['Halo', 'Enjoy the Silence', 'Clean'])
    second = total_time(violator_songs_dict, ['Sweetest Perfection', 'Policy of Truth', 'Blue Dress'])
    print('Три песни звучат', first, 'минут')
    print('А другие три песни звучат', second, 'минут')


if __name__ == '__main__':
    run()
