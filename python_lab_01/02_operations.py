# Задание 02. Знаки операций.
# Между числами 1 2 3 4 5 поставить +, -, * и скобки так, чтобы вышло 25.
# Порядок чисел не меняется.

TITLE = 'Арифметическое выражение'

EXAMPLE = '(1 + 2) * 3'
ANSWER = '1 + 2 * (3 + 4 + 5)'


def example():
    return (1 + 2) * 3


def answer():
    return 1 + 2 * (3 + 4 + 5)


def run():
    print(EXAMPLE, '=', example())
    print(ANSWER, '=', answer())


if __name__ == '__main__':
    run()
