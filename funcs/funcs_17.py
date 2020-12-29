"""
Описать функцию Sin1( x , ε ) вещественного типа
(параметры x , ε — вещественные, ε > 0),
находящую приближенное значение функции sin( x ):
sin( x ) = x – x ^3 /(3!) + x^ 5 /(5!) – ...
+ (–1) ^ n · x^( 2·n+1) /((2· n +1)!) + ... .
В сумме учитывать все слагаемые, модуль которых больше ε .
С помощью Sin1 найти приближенное значение синуса
для данного x при шести данных ε .  [01-11.3-Proc41]
"""
import math


def sin1(x, eps):
    n = 0
    value = x
    summ = 0
    while abs(value) > eps:
        f = 2 * n + 1
        new_f = 1
        for s in range(1, f + 1):
            new_f *= s
        value = (-1) ** n * x ** (2 * n + 1) / new_f
        n += 1
        summ += value
    return summ


def main():
    eps = 0.01
    number = math.pi/6
    for i in range(0, 6):
        f = sin1(number, eps)
        eps /= 10
        print(f'eps= {eps}, sin({number})= {f}')


if __name__ == '__main__':
    main()
