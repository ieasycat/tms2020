"""
Дан список чисел. Найти произведение всех чисел, которые кратны 3.
"""
from functools import reduce


def main():
    print(reduce(lambda a, x: a * x,
                 filter(lambda x: x % 3 == 0, [2, 3, 5, 6]), 1))


if __name__ == '__main__':
    main()
