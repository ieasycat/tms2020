"""
Создать lambda функцию,
которая принимает на вход неопределенное количество
именных аргументов и выводит словарь с ключами
удвоенной длины. {‘abc’: 5} -> {‘abcabc’: 5}
"""


def main():
    print((lambda **kwargs:
           {key * 2: values for key, values in kwargs.items()})
          (alo=1, allo=1, alllo=1))


if __name__ == '__main__':
    main()
