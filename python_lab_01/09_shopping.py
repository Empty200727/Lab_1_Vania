# Задание 09. Магазины со сладостями.
# Вручную составить словарь sweets: для каждого товара - 2 магазина
# с минимальной ценой.

TITLE = 'Минимальные цены на сладости'

shops = {
    'ашан': [
        {'name': 'печенье', 'price': 10.99},
        {'name': 'конфеты', 'price': 34.99},
        {'name': 'карамель', 'price': 45.99},
        {'name': 'пирожное', 'price': 67.99}
    ],
    'пятерочка': [
        {'name': 'печенье', 'price': 9.99},
        {'name': 'конфеты', 'price': 32.99},
        {'name': 'карамель', 'price': 46.99},
        {'name': 'пирожное', 'price': 59.99}
    ],
    'магнит': [
        {'name': 'печенье', 'price': 11.99},
        {'name': 'конфеты', 'price': 30.99},
        {'name': 'карамель', 'price': 41.99},
        {'name': 'пирожное', 'price': 62.99}
    ],
}

sweets = {
    'печенье': [{'shop': 'пятерочка', 'price': 9.99}, {'shop': 'ашан', 'price': 10.99}],
    'конфеты': [{'shop': 'магнит', 'price': 30.99}, {'shop': 'пятерочка', 'price': 32.99}],
    'карамель': [{'shop': 'магнит', 'price': 41.99}, {'shop': 'ашан', 'price': 45.99}],
    'пирожное': [{'shop': 'пятерочка', 'price': 59.99}, {'shop': 'магнит', 'price': 62.99}],
}


def best_shop(product):
    # Самое выгодное предложение по товару
    return sweets[product][0]


def run():
    for product, offers in sweets.items():
        print(product.upper())
        for offer in offers:
            print('   ', offer['shop'], offer['price'])
    cookie = best_shop('печенье')
    print('Печенье дешевле всего в магазине', cookie['shop'])


if __name__ == '__main__':
    run()
