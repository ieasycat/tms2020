"""
Написать функцию принимающая на вход неопределенным количеством аргументов
и именованный аргумент mean_type.
В зависимости от mean_type вернуть среднеарифметическое
либо среднегеометрическое. Написать программу в виде трех функций.
"""


def arithmetic(*args):
    arithmetic_elem = 0
    summ = 0
    for elem in args:
        summ += elem
    arithmetic_elem = summ / len(args)
    return arithmetic_elem


def geometric(*args):
    geometric_elem = 0
    summ = 1
    for elem in args:
        summ *= elem
    geometric_elem = summ ** (1/len(args))
    return geometric_elem


def choice(mean_type, *args):
    if mean_type == 'arithmetic':
        print(f'Среднеарифметическое значение равно - {arithmetic(*args)}')

    elif mean_type == 'geometric':
        print(f'Среднегеометрическое значение равно - {geometric(*args)}')


def main():
    choice('geometric', 2, 4, 6, 9, 10, 11, 7, 12)


if __name__ == '__main__':
    main()
