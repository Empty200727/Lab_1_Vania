# Задание 08. Сад и луг.
# Сделать множества цветов и вывести: все виды; общие; только в саду;
# только на лугу.

from collections import namedtuple

TITLE = 'Множества цветов'

garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

FlowerReport = namedtuple('FlowerReport', ['every', 'both', 'garden_only', 'meadow_only'])


def compare(garden_flowers, meadow_flowers):
    g = set(garden_flowers)
    m = set(meadow_flowers)
    return FlowerReport(g | m, g & m, g - m, m - g)


def run():
    report = compare(garden, meadow)
    print('Все цветы:', ', '.join(sorted(report.every)))
    print('И в саду, и на лугу:', ', '.join(sorted(report.both)))
    print('Только в саду:', ', '.join(sorted(report.garden_only)))
    print('Только на лугу:', ', '.join(sorted(report.meadow_only)))


if __name__ == '__main__':
    run()
