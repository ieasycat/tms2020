"""
Создать статичный метод get_random_name для класса Pet.
Метод возвращает случайную строку вида A-42.
"""
import string
from random import choice, randint
from abc import ABC, abstractmethod


class Pet(ABC):
    __counter = 0

    def __init__(self, name, age, master, weight, height):
        self.name = name
        self.age = age
        self.master = master
        self.weight = weight
        self.height = height
        Pet.__counter += 1

    @classmethod
    def get_counter(cls):
        return cls.__counter

    @staticmethod
    def run(self):
        print('Run!')

    def jump(self, high):
        print(f'Jump {high} meters')

    def birthday(self):
        self.age += 1

    @staticmethod
    def sleep(self):
        print('Sleep!')

    def change_weight(self, weight=0.2):
        self.weight += weight

    def change_height(self, height=0.2):
        self.height += height

    @abstractmethod
    def voice(self):
        pass

    def __eq__(self, other):
        return all(
            [self.age == other.age,
             self.weight == other.weight,
             self.height == other.height,
             type(self) == type(other)]
        )

    def __ne__(self, other):
        return not self == other

    @staticmethod
    def get_random_name():
        return f'{choice(string.ascii_lowercase)}-' \
               f'{randint(0, 9)}' \
               f'{randint(0, 9)}'


class Dog(Pet):
    def jump(self, high):
        if high > 0.5:
            print('Dogs cannot jump so high')
        else:
            super().jump(high)

    def voice(self):
        print('Bark!')


class Cat(Pet):
    def jump(self, high):
        if high > 2:
            print('Cats cannot jump so high')
        else:
            super().jump(high)

    def voice(self):
        print('Meow!')


class Parrot(Pet):
    def __init__(self, name, age, master, weight, height, species):
        super(Parrot, self).__init__(name, age, master, weight, height)
        self.species = species

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

    def voice(self):
        print('AAaaAaaAaA')


def voice_challenge(list_animals):
    for i in list_animals:
        i.voice()


class Horse(Pet):
    def voice(self):
        print('Igogo')


class Donkey(Pet):
    def voice(self):
        print('Iaiaia')


class Mule(Donkey, Horse):
    def voice(self):
        super(Mule, self).voice()


def main():
    Mule('Ia', 4, 'Alex', 3, 3)
    Mule('Freek', 4, 'Dima', 4, 3)
    Mule('Freek', 4, 'Olya', 3, 3)
    print(Pet.get_random_name())
    # error = Pet('Zaika', 3, 'Riki', 3, 3)


if __name__ == '__main__':
    main()
