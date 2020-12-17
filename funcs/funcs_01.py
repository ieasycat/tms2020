"""
Написать функцию, которая получает на вход имя и
выводит строку вида: “Hello, {name}”.
Создать список из 5 имен. Вызвать функцию для каждого элемента списка в цикле.
"""

name_list = ['Anton', 'Dima', 'Volodya', 'Gleb', 'Katya']


def hello(name):
    print(f'Hello, {name}')


for i in name_list:
    hello(i)
