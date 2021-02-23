"""
Создать бесконечный генератор случайных чисел.
Генератор должен принимать диапазон случайных чисел и смещение
Пример: a = 1, b = 10, diff = 10
1- 10
11-20
…
N +10 - M + 10
"""

from random import randint
from time import sleep


def my_random_numbers(a=1, b=10, diff=10):
    while True:
        yield randint(a, b)
        a += diff
        b += diff
        sleep(1)


def main():
    random_numb = my_random_numbers()
    for numb in random_numb:
        print(numb)


if __name__ == '__main__':
    main()
