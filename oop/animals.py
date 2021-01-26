"""
Создать файл animals.py.
Создать три класса: Dog, Cat, Parrot.
Атрибуты каждого класса: name, age, master.
Каждый класс содержит конструктор и методы: run, jump,
birthday(увеличивает age на 1), sleep.
Класс Parrot имеет дополнительный метод fly. Cat - meow, Dog - bark.
"""


class Dog:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        print('Run Dog!')

    def jump(self):
        print('Jump Dog')

    def birthday(self):
        self.age += 1

    def sleep(self):
        print('Sleep Dog')

    def bark(self):
        print('Bark')


class Cat:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        print('Run Cat!')

    def jump(self):
        print('Jump Cat')

    def birthday(self):
        self.age += 1

    def meow(self):
        print('Meow')

    def sleep(self):
        print('Sleep Cat')


class Parrot:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        print('Run Parrot!')

    def jump(self):
        print('Jump Parrot')

    def birthday(self):
        self.age += 1

    def sleep(self):
        print('Sleep Parrot')

    def fly(self):
        print('Fly')


def main():
    pass


if __name__ == '__main__':
    main()
