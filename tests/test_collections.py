# Тесты заданий 05-10
from helpers import get

zoo = get('05_zoo')
songs = get('06_songs_list')
secret = get('07_secret')
garden = get('08_garden')
shopping = get('09_shopping')
store = get('10_store')


def test_zoo():
    animals = zoo.remove_elephant(zoo.add_birds(zoo.add_bear(zoo.zoo), zoo.birds))
    assert animals == ['lion', 'bear', 'kangaroo', 'monkey', 'rooster', 'ostrich', 'lark']
    assert zoo.cages(animals)['lion'] == 1
    assert zoo.cages(animals)['lark'] == 7


def test_zoo_source_not_changed():
    zoo.remove_elephant(zoo.add_bear(zoo.zoo))
    assert zoo.zoo == ['lion', 'kangaroo', 'elephant', 'monkey']


def test_songs():
    assert songs.total_time(songs.violator_songs_list, ['Halo', 'Enjoy the Silence', 'Clean']) == 14.93
    assert songs.total_time(
        songs.violator_songs_dict, ['Sweetest Perfection', 'Policy of Truth', 'Blue Dress']
    ) == 13.49


def test_secret():
    assert secret.decrypt(secret.secret_message) == 'в бане веник дороже денег'


def test_garden():
    report = garden.compare(garden.garden, garden.meadow)
    assert report.both == {'ромашка', 'одуванчик'}
    assert report.garden_only == {'роза', 'гладиолус', 'подсолнух'}
    assert report.meadow_only == {'клевер', 'мак'}
    assert report.every == report.both | report.garden_only | report.meadow_only


def test_sweets_are_really_cheapest():
    for product, offers in shopping.sweets.items():
        prices = sorted(
            item['price']
            for items in shopping.shops.values()
            for item in items
            if item['name'] == product
        )
        assert [offer['price'] for offer in offers] == prices[:2]


def test_store():
    assert store.count_product('12345') == (27, 1134)
    assert store.count_product('45678') == (105, 10311)
    assert store.report_lines()[1] == 'Стол - 54 шт, стоимость 27860 руб'
    assert store.report_lines()[2] == 'Диван - 3 шт, стоимость 3550 руб'


def test_store_run_prints_four_lines(capsys):
    store.run()
    lines = capsys.readouterr().out.strip().split('\n')
    assert len(lines) == 4
    assert lines[0] == 'Лампа - 27 шт, стоимость 1134 руб'
