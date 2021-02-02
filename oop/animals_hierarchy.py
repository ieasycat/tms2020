"""
Создать файл animals_hierarchy.py. Реализовать следующую структуру.
"""
from abc import ABC, abstractmethod


class Animal:
    pass


class FelineInterface(ABC):
    @abstractmethod
    def feline(self, arg1):
        raise NotImplementedError


class CanineInterface(ABC):
    @abstractmethod
    def canine(self, arg1):
        raise NotImplementedError


class Pet(Animal):
    pass


class Cat(Pet, FelineInterface):
    def feline(self, feature='The sound of scratching.'):
        return feature


class Dog(Pet, CanineInterface):
    def canine(self, feature='Howl at the moon!'):
        return feature


class WildAnimal(Animal):
    pass


class Lion(WildAnimal, FelineInterface):
    def feline(self, feature='The sound of scratching.'):
        return feature


class Wolf(WildAnimal, CanineInterface):
    def canine(self, feature='Howl at the moon!'):
        return feature


def main():
    my_cat = Cat()
    print(f"This's Cat - {my_cat.feline()}")
    my_lion = Lion()
    print(f"This's Lion - {my_lion.feline()}")

    my_dog = Dog()
    print(f"This's Dog - {my_dog.canine()}")
    my_wolf = Wolf()
    print(f"This's Wolf - {my_wolf.canine()}")


if __name__ == '__main__':
    main()
