"""
Создать файл animals.py.
Создать три класса: Dog, Cat, Parrot.
Атрибуты каждого класса: name, age, master.
Каждый класс содержит конструктор и методы: run, jump,
birthday(увеличивает age на 1), sleep.
Класс Parrot имеет дополнительный метод fly. Cat - meow, Dog - bark.
"""


class Pet:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        print('Run!')

    def jump(self):
        print('Jump!')

    def birthday(self):
        self.age += 1

    def sleep(self):
        print('Sleep!')


class Dog(Pet):
    def bark(self):
        print('Bark!')


class Cat(Pet):
    def meow(self):
        print('Meow!')


class Parrot(Pet):
    def fly(self):
        print('Fly!')


def main():
    my_cat = Cat('Barsik', 10, 'Anton')
    my_cat.run()
    my_cat.meow()


if __name__ == '__main__':
    main()
