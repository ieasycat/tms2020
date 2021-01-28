"""
Унаследовать от класса Pet два класса: Horse, Donkey.
Переопределить в классах методы voice.
Создать класс Mule.
Метод voice должен быть унаследован от класса Donkey
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

    def __eq__(self, other):
        return all(
            [self.age == other.age,
             self.weight == other.weight,
             self.height == other.height,
             type(self) == type(other)]
        )

    def __ne__(self, other):
        return not self == other


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
    not_my_mule = Mule('Ia', 4, 'Alex', 3, 3)
    not_my_mule_2 = Mule('Freek', 4, 'Dima', 4, 3)
    not_my_mule_3 = Mule('Freek', 4, 'Olya', 3, 3)
    print(not_my_mule == not_my_mule_3)
    print(not_my_mule_2 != not_my_mule_3)
    not_my_mule.voice()


if __name__ == '__main__':
    main()
