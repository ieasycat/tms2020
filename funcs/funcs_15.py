"""
Описать функцию fact2( n ), вычисляющую двойной факториал
:n!! = 1·3·5·...·n, если n — нечетное; n!! = 2·4·6·...·n,
если n — четное (n > 0 — параметр целого типа.
С помощью этой функции найти двойные факториалы пяти данных целых чисел
"""


def fact2(n):
    summ = 1
    if n % 2 == 0:
        for number in range(2, n + 1, 2):
            summ *= number
    else:
        for number in range(1, n + 1, 2):
            summ *= number
    return summ


def main():
    one = fact2(10)
    two = fact2(15)
    three = fact2(20)
    four = fact2(25)
    five = fact2(30)
    print(f'{one} - это факториал "10", {two} - это "15", {three} - это "20"'
          f', {four} - это "25", а {five} - это "30" ')


if __name__ == '__main__':
    main()
