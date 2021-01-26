"""
Добавить метод jump, принимающий высоту прыжка.
Метод выводит сообщение “Jump X meters”
Переопределить метод jump в дочерних классах.
Если передать методу jump класса dog значение больше 0.5,
выводить сообщение “Dogs cannot jump so high,
аналогично для кошек(2), для попугаев(0.05)
"""


class Pet:
    def __init__(self, name, age, master, weight, height):
        self.name = name
        self.age = age
        self.master = master
        self.weight = weight
        self.height = height

    def run(self):
        print('Run!')

    def jump(self, high):
        print(f'Jump {high} meters')

    def birthday(self):
        self.age += 1

    def sleep(self):
        print('Sleep!')

    def change_weight(self, weight=0.2):
        self.weight += weight

    def change_height(self, height=0.2):
        self.height += height


class Dog(Pet):
    def jump(self, high):
        if high > 0.5:
            print('Dogs cannot jump so high')
        else:
            super().jump(high)

    def bark(self):
        print('Bark!')


class Cat(Pet):
    def jump(self, high):
        if high > 2:
            print('Cats cannot jump so high')
        else:
            super().jump(high)

    def meow(self):
        print('Meow!')


class Parrot(Pet):
    def jump(self, high):
        if high > 0.05:
            print('Parrot cannot jump so high')
        else:
            super().jump(high)

    def change_weight(self, weight=0.05):
        self.weight += weight

    def change_height(self, height=0.05):
        self.height += height

    def fly(self):
        if self.weight > 0.1:
            print('This parrot cannot fly.')
        else:
            print('Fly!')


def main():
    my_cat = Cat('Barsik', 10, 'Anton', 4, 3)
    my_cat.run()
    my_cat.meow()
    my_cat.jump(1)
    my_cat.jump(3)


if __name__ == '__main__':
    main()
