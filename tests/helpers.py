import importlib


def get(name):
    return importlib.import_module('python_lab_01.' + name)
