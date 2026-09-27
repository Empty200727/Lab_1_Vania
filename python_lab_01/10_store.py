# Задание 10. Склад.
# Для каждого товара посчитать количество и общую стоимость всех партий,
# вывод: <товар> - <кол-во> шт, стоимость <сумма> руб

TITLE = 'Остатки на складе'

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}


def count_product(code):
    quantity = 0
    cost = 0
    for part in store[code]:
        quantity = quantity + part['quantity']
        cost = cost + part['quantity'] * part['price']
    return quantity, cost


def report_lines():
    lines = []
    for title in goods:
        quantity, cost = count_product(goods[title])
        lines.append(f'{title} - {quantity} шт, стоимость {cost} руб')
    return lines


def run():
    print('\n'.join(report_lines()))


if __name__ == '__main__':
    run()
