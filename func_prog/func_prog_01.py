"""
Создать lambda функцию,
которая принимает на вход имя и выводит его в формате “Hello, {name}”
"""


def my_lambda():
    return (lambda name: f'Hello, {name}')('Anton')


def main():
    pr = my_lambda()
    print(pr)


if __name__ == '__main__':
    main()
