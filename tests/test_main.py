# Проверка главного модуля
import main


def test_all_tasks_found():
    names = [path.stem for path in main.task_files()]
    assert len(names) == 11
    assert names[0] == '00_distance'
    assert names[-1] == '10_store'


def test_every_task_has_run_and_title():
    for path in main.task_files():
        module = main.load(path)
        assert callable(module.run)
        assert module.TITLE


def test_main_output(capsys):
    main.main()
    out = capsys.readouterr().out
    assert out.count('Задание') == 11
    assert 'в бане веник дороже денег' in out
    assert 'Стул - 105 шт, стоимость 10311 руб' in out
