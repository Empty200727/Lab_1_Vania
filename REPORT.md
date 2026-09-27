<div align="center">

Министерство образования и науки РФ

Федеральное государственное бюджетное образовательное учреждение высшего образования
«Тверской государственный технический университет»
(ФГБОУ ВО «ТвГТУ»)

Кафедра программного обеспечения

<br><br><br><br>

### Лабораторная работа № 1

по дисциплине «Теория алгоритмов»

«Введение в язык программирования Python»

</div>

<br><br><br>

<div align="right">

Выполнил: студент 3 курса
группы Б.ПИН.РИС-24.06
**[ФИО СТУДЕНТА]**

Проверила: Лисничук А. Б.

</div>

<br><br><br>

<div align="center">

Тверь, 2026

</div>

---

## Оглавление

- 1 Цель и задание
- 2 Выполнение работы
  - 2.1 Подготовка рабочего места
  - 2.2 Задания
    - 2.2.1 Расстояния между городами (00_distance.py)
    - 2.2.2 Круг и точки (01_circle.py)
    - 2.2.3 Знаки операций (02_operations.py)
    - 2.2.4 Любимые фильмы (03_favorite_movies.py)
    - 2.2.5 Моя семья (04_my_family.py)
    - 2.2.6 Зоопарк (05_zoo.py)
    - 2.2.7 Песни (06_songs_list.py)
    - 2.2.8 Секретное сообщение (07_secret.py)
    - 2.2.9 Сад и луг (08_garden.py)
    - 2.2.10 Сладости (09_shopping.py)
    - 2.2.11 Склад (10_store.py)
  - 2.3 Главный модуль
  - 2.4 Тесты
- 3 Команды Git
- 4 Скриншоты
- 5 Заключение
- 6 Использованные источники

---

## 1 Цель и задание

**Цель:** научиться писать простые программы на Python, работать со строками и
коллекциями, хранить проект в Git и проверять код тестами.

Задание разбито на три уровня.

*Уровень Rare* – обязательная часть:

1. Поставить Python и настроить его.
2. Создать на GitHub репозиторий для предмета и склонировать его себе.
3. Распаковать в репозиторий архив с 11 задачами и решить их.
4. Добавить `README.md` и `requirements.txt`.
5. Написать отчёт: задание, описание работы, код, скриншоты, команды Git, источники.
6. Сделать commit и push.

*Уровень Medium* – сделать главный модуль, который пользуется кодом заданий.
Для этого код каждого задания нужно убрать в функции.

*Уровень Well-done* – написать тесты на pytest.

Ссылка на репозиторий: **[ССЫЛКА НА РЕПОЗИТОРИЙ]**

## 2 Выполнение работы

### 2.1 Подготовка рабочего места

Установлен Python 3.13, в качестве среды разработки выбран PyCharm Community.
При создании проекта PyCharm сам сделал виртуальное окружение `.venv`.

Репозиторий склонирован с GitHub, работа велась в отдельной ветке `lab-01`.
В `.gitignore` добавлены папка настроек PyCharm `.idea/`, окружение `.venv/`
и кэши `__pycache__/`, `.pytest_cache/`, чтобы они не попадали в коммиты.

Pytest поставлен командой `pip install pytest`, после чего все пакеты окружения
записаны в файл командой `pip freeze > requirements.txt`. Чтобы развернуть
проект заново, достаточно выполнить `pip install -r requirements.txt`.

### 2.2 Задания

Задачи лежат в папке `python_lab_01`. В начале каждого файла в комментарии
кратко записано условие, затем идут данные, функции с решением и функция
`run()`, которая печатает ответ. Ещё в каждом файле есть строка `TITLE` с
названием задания – она нужна главному модулю для заголовков.

#### 2.2.1 Расстояния между городами (00_distance.py)

Для каждого города перебираются все остальные города, и расстояние между ними
считается по теореме Пифагора с помощью `math.sqrt`. Сам с собой город не
сравнивается. Значения округлены до трёх знаков, чтобы вывод было удобно читать.

```python
def get_distance(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return math.sqrt(dx ** 2 + dy ** 2)


def get_distances(points):
    distances = dict()
    for town, coords in points.items():
        distances[town] = dict()
        for other_town, other_coords in points.items():
            if other_town != town:
                distances[town][other_town] = round(get_distance(coords, other_coords), 3)
    return distances
```

**[СКРИНШОТ: вывод 00_distance.py]**

*Рис. 1. Работа программы 00_distance.py*

#### 2.2.2 Круг и точки (01_circle.py)

Площадь – это π·r², результат сразу округляется до 4 знаков. Чтобы узнать,
попадает ли точка в круг, считается её расстояние до центра (0, 0) и
сравнивается с радиусом. Координаты точки передаются в функцию распаковкой
`*point`.

```python
def get_area(r):
    return round(PI * r ** 2, 4)


def distance_from_center(x, y):
    return math.sqrt(x ** 2 + y ** 2)


def inside(point, r=radius):
    return distance_from_center(*point) <= r
```

**[СКРИНШОТ: вывод 01_circle.py]**

*Рис. 2. Работа программы 01_circle.py*

#### 2.2.3 Знаки операций (02_operations.py)

Подходящее выражение: 1 + 2 · (3 + 4 + 5). В скобках получается 12, умножение
на 2 даёт 24, плюс 1 – ровно 25. Выражение хранится ещё и строкой, чтобы
вывести его на экран вместе с ответом.

```python
EXAMPLE = '(1 + 2) * 3'
ANSWER = '1 + 2 * (3 + 4 + 5)'


def example():
    return (1 + 2) * 3


def answer():
    return 1 + 2 * (3 + 4 + 5)
```

**[СКРИНШОТ: вывод 02_operations.py]**

*Рис. 3. Работа программы 02_operations.py*

#### 2.2.4 Любимые фильмы (03_favorite_movies.py)

Сначала срезами вырезаются все пять названий, при этом запятые и пробелы
остаются за границами срезов. Потом из полученного списка берутся нужные
элементы: `[0]`, `[-1]`, `[1]` и `[-2]`.

```python
def cut_titles(movies):
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
```

**[СКРИНШОТ: вывод 03_favorite_movies.py]**

*Рис. 4. Работа программы 03_favorite_movies.py*

#### 2.2.5 Моя семья (04_my_family.py)

Список `my_family_height` собирается из двух списков – имён и ростов – с помощью
`zip()`. Позиция папы находится методом `index()`, рост всей семьи считается
функцией `sum()`.

```python
my_family = ['Папа', 'Мама', 'Сестра', 'Бабушка', 'Я']
heights = [181, 168, 163, 158, 176]

my_family_height = [[name, h] for name, h in zip(my_family, heights)]


def father_height(family, family_height):
    position = family.index('Папа')
    return family_height[position][1]


def sum_height(family_height):
    return sum(h for _, h in family_height)
```

**[СКРИНШОТ: вывод 04_my_family.py]**

*Рис. 5. Работа программы 04_my_family.py*

#### 2.2.6 Зоопарк (05_zoo.py)

Каждое действие вынесено в свою функцию, и каждая функция возвращает новый
список, не трогая исходный. Медведь ставится сразу после льва склейкой срезов,
птицы добавляются сложением списков, слон удаляется методом `pop()`. Номера
клеток получаются через `enumerate(..., start=1)`.

```python
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
```

**[СКРИНШОТ: вывод 05_zoo.py]**

*Рис. 6. Работа программы 05_zoo.py*

#### 2.2.7 Песни (06_songs_list.py)

Обе части задания решаются одной функцией. Если на вход пришёл список пар,
он превращается в словарь через `dict()`, а дальше длительности просто
складываются по названиям. Сумма округляется до 3 знаков.

```python
def total_time(songs, names):
    if isinstance(songs, list):
        songs = dict(songs)
    result = 0.0
    for name in names:
        result += songs[name]
    return round(result, 3)
```

**[СКРИНШОТ: вывод 06_songs_list.py]**

*Рис. 7. Работа программы 06_songs_list.py*

#### 2.2.8 Секретное сообщение (07_secret.py)

Правила расшифровки записаны таблицей `RULES`: номер строки, начало, конец и
шаг среза (номера букв уже переведены в индексы). В цикле из каждой строки
вырезается слово и приклеивается к фразе. Результат – «в бане веник дороже
денег».

```python
RULES = [
    (0, 3, 4, 1),
    (1, 9, 13, 1),
    (2, 5, 15, 2),
    (3, 12, 6, -1),
    (4, 20, 15, -1),
]


def decrypt(message):
    phrase = ''
    for row, start, stop, step in RULES:
        phrase += message[row][start:stop:step] + ' '
    return phrase.strip()
```

**[СКРИНШОТ: вывод 07_secret.py]**

*Рис. 8. Работа программы 07_secret.py*

#### 2.2.9 Сад и луг (08_garden.py)

Из кортежей делаются множества, дальше используются операторы `|` (объединение),
`&` (пересечение) и `-` (разность). Все четыре ответа возвращаются одним
именованным кортежем `FlowerReport`. При печати множества сортируются, чтобы
порядок цветов не менялся от запуска к запуску.

```python
FlowerReport = namedtuple('FlowerReport', ['every', 'both', 'garden_only', 'meadow_only'])


def compare(garden_flowers, meadow_flowers):
    g = set(garden_flowers)
    m = set(meadow_flowers)
    return FlowerReport(g | m, g & m, g - m, m - g)
```

**[СКРИНШОТ: вывод 08_garden.py]**

*Рис. 9. Работа программы 08_garden.py*

#### 2.2.10 Сладости (09_shopping.py)

Словарь `sweets` составлен вручную: для каждого товара записаны два магазина с
самыми низкими ценами, по возрастанию цены. Поэтому самый выгодный магазин –
всегда первый элемент списка, что и использует функция `best_shop()`.

```python
sweets = {
    'печенье': [{'shop': 'пятерочка', 'price': 9.99}, {'shop': 'ашан', 'price': 10.99}],
    'конфеты': [{'shop': 'магнит', 'price': 30.99}, {'shop': 'пятерочка', 'price': 32.99}],
    'карамель': [{'shop': 'магнит', 'price': 41.99}, {'shop': 'ашан', 'price': 45.99}],
    'пирожное': [{'shop': 'пятерочка', 'price': 59.99}, {'shop': 'магнит', 'price': 62.99}],
}


def best_shop(product):
    return sweets[product][0]
```

**[СКРИНШОТ: вывод 09_shopping.py]**

*Рис. 10. Работа программы 09_shopping.py*

#### 2.2.11 Склад (10_store.py)

Функция `count_product()` по коду товара проходит все его партии и
накапливает количество и стоимость (количество × цена). Функция
`report_lines()` собирает готовые строки отчёта в нужном формате.

```python
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
```

**[СКРИНШОТ: вывод 10_store.py]**

*Рис. 11. Работа программы 10_store.py*

### 2.3 Главный модуль

Чтобы выполнить уровень Medium, весь код заданий был разложен по функциям.
Печать осталась только в `run()`, а её вызов стоит внутри
`if __name__ == '__main__':`. Если файл запустить напрямую, задание
выполнится; если его подключить из другого модуля – ничего лишнего не
напечатается.

Проблема в том, что имена файлов начинаются с цифр, и написать
`import 00_distance` нельзя – это синтаксическая ошибка. Поэтому в `main.py`
модули загружаются прямо по пути к файлу средствами `importlib.util`:
`spec_from_file_location()` создаёт описание модуля, `module_from_spec()` –
пустой модуль, а `exec_module()` выполняет в нём код файла. Список файлов
собирается через `Path.glob()` по маске `[0-9][0-9]_*.py`.

```python
TASKS_DIR = Path(__file__).parent / 'python_lab_01'


def task_files():
    return sorted(TASKS_DIR.glob('[0-9][0-9]_*.py'))


def load(path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    for path in task_files():
        module = load(path)
        print('=' * 50)
        print(f'Задание {path.stem[:2]}: {module.TITLE}')
        print('=' * 50)
        module.run()
        print()
```

При запуске `python main.py` по очереди выполняются все 11 заданий, перед
каждым печатается заголовок с номером и названием.

### 2.4 Тесты

Для уровня Well-done написаны тесты на pytest. Они разделены на три файла:

| Файл | Что проверяет |
|---|---|
| `tests/test_basics.py` | задания 00–04 |
| `tests/test_collections.py` | задания 05–10 |
| `tests/test_main.py` | главный модуль |

В `pytest.ini` указано `pythonpath = .`, поэтому пакет `python_lab_01` и
`main.py` видны из тестов без дополнительных настроек. Модули с цифрами в
имени подключаются маленькой функцией `get()` из `tests/helpers.py`, которая
вызывает `importlib.import_module()`.

Кроме проверки ответов, тесты проверяют, что исходный список зоопарка не
портится, что словарь `sweets` действительно содержит минимальные цены
(они пересчитываются из `shops` прямо в тесте), а также что `main.py` находит
все 11 заданий и печатает их результаты (вывод ловится фикстурой `capsys`).

```python
def test_sweets_are_really_cheapest():
    for product, offers in shopping.sweets.items():
        prices = sorted(
            item['price']
            for items in shopping.shops.values()
            for item in items
            if item['name'] == product
        )
        assert [offer['price'] for offer in offers] == prices[:2]


def test_main_output(capsys):
    main.main()
    out = capsys.readouterr().out
    assert out.count('Задание') == 11
    assert 'в бане веник дороже денег' in out
```

Команда `pytest -v` нашла 18 тестов, все прошли – **18 passed**.

**[СКРИНШОТ: результат pytest -v]**

*Рис. 12. Результат запуска тестов*

## 3 Команды Git

Ниже перечислены команды, которыми я пользовался при выполнении работы.

- `git clone https://github.com/...` – скачать репозиторий с GitHub на компьютер.
- `git checkout -b lab-01` – создать ветку `lab-01` и перейти на неё.
- `git status` – узнать, какие файлы изменены и что уже добавлено к коммиту.
- `git add python_lab_01/` – добавить к коммиту изменения в папке.
- `git add -A` – добавить вообще все изменения, включая удалённые файлы.
- `git commit -m "сообщение"` – сохранить изменения в истории с описанием.
- `git log` – посмотреть историю коммитов.
- `git remote -v` – посмотреть, к какому удалённому репозиторию привязан проект.
- `git push --set-upstream origin lab-01` – в первый раз отправить ветку на GitHub и связать её с удалённой.
- `git push` – отправлять следующие коммиты.
- `git pull` – подтянуть изменения, сделанные на GitHub или с другого компьютера.
- `git restore <файл>` – отменить незакоммиченные изменения в файле.

Чтобы Git не видел лишние файлы, в корне проекта лежит `.gitignore` с папками
`.idea/`, `.venv/`, `__pycache__/` и `.pytest_cache/`.

## 4 Скриншоты

Запуск всех заданий через `main.py` показан на рисунке 13.

**[СКРИНШОТ: вывод python main.py]**

*Рис. 13. Работа главного модуля*

## 5 Заключение

В лабораторной работе я познакомился с языком Python: попробовал арифметику,
срезы строк, списки, кортежи, словари и множества, а также модули стандартной
библиотеки `math`, `collections`, `importlib` и `pathlib`. Все 11 заданий
решены.

Код заданий разложен по функциям, благодаря чему его удалось подключить в
главный модуль `main.py`, который запускает все задания подряд. Правильность
решений подтверждают 18 тестов pytest, все они проходят. В репозитории есть
`README.md`, `requirements.txt` и `.gitignore`.

Ссылка на репозиторий: **[ССЫЛКА НА РЕПОЗИТОРИЙ]**

## 6 Использованные источники

1. Документация Python 3 на русском [Электронный ресурс]. – URL: https://docs.python.org/ru/3/ (дата обращения: 08.09.2026).
2. importlib.util — утилиты для импорта [Электронный ресурс]. – URL: https://docs.python.org/3/library/importlib.html#module-importlib.util (дата обращения: 09.09.2026).
3. Get Started — pytest documentation [Электронный ресурс]. – URL: https://docs.pytest.org/en/stable/getting-started.html (дата обращения: 11.09.2026).
4. GitHub Docs: Про Git [Электронный ресурс]. – URL: https://docs.github.com/ru/get-started/using-git/about-git (дата обращения: 11.09.2026).
5. Основной синтаксис Markdown [Электронный ресурс]. – URL: https://www.markdownguide.org/basic-syntax/ (дата обращения: 13.09.2026).
