"""файл модуль libs"""


def get_count(string, symbol):
    """
    Функция считает колличество указанных символов в  строке.
    """
    cnt = 0
    for i in string:
        if i == symbol:
            cnt += 1
    return cnt


def get_len(string):
    """
    Функция считает колличество всех символов в  строке.
    """
    cnt = 0
    for i in string:
        cnt += 1
    return cnt


if __name__ == '__main__':
    """
    Данное условие выполяется только когда отрабатывает этот файл как отдельный скрипт.
    Если файл подключить как модуль то код ниже не выполняется.
    """
    print(__name__)  # в __main__
    print('file libs.py')  # просто выведется принт
