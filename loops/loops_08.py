"""
Ввести два целых числа a и b ( a < b ).
Вывести в порядке возрастания все целые числа,
расположенные между a и b (включая сами числа a и b ),
а также количество n этих чисел. [01-08-For2]
"""


def numbers(a, b):
    count = 0
    if not a > b:
        for i in range(a, b + 1):
            count += 1
            print(i)
    print(f'Количество чисел между {a} и {b} - {count}')


def main():
    a = int(input("Введите 1-ое число: "))
    b = int(input("Введите 2-ое число: "))
    numbers(a, b)


if __name__ == '__main__':
    main()
