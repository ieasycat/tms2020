"""
Создать скрипт,
который при запуске принимает неопределенное количество аргументов
и считает сумму тех из них, что являются цифрами.
Пример:
python test.py 1 2 3 4 a b 5 6 -->  21
"""

import sys


def summ(args):
    my_summ = 0
    print(args)
    for number in args[1:]:
        if number.isdigit():
            my_summ += int(number)
    return my_summ


def main():
    print(summ(sys.argv))


if __name__ == '__main__':
    main()
