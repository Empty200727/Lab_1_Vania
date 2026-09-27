# Задание 05. Зоопарк.
# Медведя - между львом и кенгуру, птиц - в конец, слона - убрать.
# Потом вывести номера клеток льва и жаворонка (счёт с 1).

TITLE = 'Зоопарк'

zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
birds = ['rooster', 'ostrich', 'lark']


def add_bear(animals):
    lion = animals.index('lion')
    return animals[:lion + 1] + ['bear'] + animals[lion + 1:]


def add_birds(animals, new_birds):
    return animals + new_birds


def remove_elephant(animals):
    result = animals[:]
    result.pop(result.index('elephant'))
    return result


def cages(animals):
    return {animal: number for number, animal in enumerate(animals, start=1)}


def run():
    step_1 = add_bear(zoo)
    print(step_1)
    step_2 = add_birds(step_1, birds)
    print(step_2)
    step_3 = remove_elephant(step_2)
    print(step_3)

    numbers = cages(step_3)
    print('lion - клетка', numbers['lion'])
    print('lark - клетка', numbers['lark'])


if __name__ == '__main__':
    run()
