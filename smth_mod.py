## functions модуль для импорта функций для работы

# TODO - import <зависимость из задания>


def _to_tuple(l):
    """Функция 1"""
    return tuple(l)


def multiply(n):
    """Функция 2"""
    with open("file_name.txt", "w") as f:
        f.write(str(_to_tuple(n)*2))
