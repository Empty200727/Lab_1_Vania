# Главный модуль ЛР №1: по очереди запускает все задания из папки python_lab_01.
# Файлы называются с цифры (00_distance.py ...), поэтому они подключаются
# не через import, а загрузкой по пути к файлу (importlib.util).

import importlib.util
from pathlib import Path

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


if __name__ == '__main__':
    main()
