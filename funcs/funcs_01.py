"""
Написать функцию, которая получает на вход имя и
выводит строку вида: “Hello, {name}”.
Создать список из 5 имен. Вызвать функцию для каждого элемента списка в цикле.
"""


def hello(name):
    print(f'Hello, {name}')


def main():
    name_list = ['Anton', 'Dima', 'Volodya', 'Gleb', 'Katya']
    for name in name_list:
        hello(name)


if __name__ == '__main__':
    main()
