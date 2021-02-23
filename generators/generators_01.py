"""
Создать бесконечный генератор случайных чисел.
Использовать в генераторе временную задержку
from time import sleep
"""

from time import sleep
from random import randint


def my_random_numbers():
    while True:
        yield randint(1, 9)
        sleep(1)


def main():
    random_numb = my_random_numbers()
    for numb in random_numb:
        print(numb)


if __name__ == '__main__':
    main()
