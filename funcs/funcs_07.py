"""
Создать функцию, которая принимает на вход неопределенное количество
именованных аргументов и выводит на экран те из них,
длина ключа которых четна.
"""


def even(**kwargs):
    for key, value in kwargs.items():
        if len(key) % 2 == 0:
            print(f'Это ключ - {key}, а это его значение - {value}')


def main():
    even(a='cat', home='book', c='door', driver='var')


if __name__ == '__main__':
    main()
