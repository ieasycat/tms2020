"""
Добавить в класс Pet пустой метод voice.
Заменить имена методов bark, meow на voice.
Добавить voice для класса Parrot.
Создать функцию, принимающая список животных и
вызывающая у каждого животного метод voice.
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

    def voice(self):
        pass


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


def main():
    my_cat = Cat('Barsik', 7, 'Dima', 8, 3)
    my_dog = Dog('Bobik', 6, 'Oleg', 8, 4)
    not_my_parrot = Parrot('Alex', 3, 'Anton', 0.5, 1, 'Phoenix')
    animals = [my_cat, my_dog, not_my_parrot]
    voice_challenge(animals)


if __name__ == '__main__':
    main()
