# Задание 04. Моя семья.
# Список членов семьи и список списков [имя, рост].
# Вывести рост отца и общий рост семьи.

TITLE = 'Рост членов семьи'

my_family = ['Папа', 'Мама', 'Сестра', 'Бабушка', 'Я']
heights = [181, 168, 163, 158, 176]

my_family_height = [[name, h] for name, h in zip(my_family, heights)]


def father_height(family, family_height):
    position = family.index('Папа')
    return family_height[position][1]


def sum_height(family_height):
    return sum(h for _, h in family_height)


def run():
    print('Рост отца -', father_height(my_family, my_family_height), 'см')
    print('Общий рост моей семьи -', sum_height(my_family_height), 'см')


if __name__ == '__main__':
    run()
