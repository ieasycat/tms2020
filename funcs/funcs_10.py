"""
Рассчитать значение х определив и использовав необходимую функции.
"""


def calc(n):
    return (n ** 1/2 + n) / 2


def main():
    result = calc(5) + calc(12) + calc(19)
    print(result)


if __name__ == '__main__':
    main()
