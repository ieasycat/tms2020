"""
Дан список чисел. Вернуть список, где каждый число переведено в строку
[5, 3] -> [‘5’, ‘3’]
"""


def main():
    two_numbers = list(map(str, [1, 2, 3, 4, 5]))
    print(two_numbers)


if __name__ == '__main__':
    main()
