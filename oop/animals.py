"""
Переопределить методы change_weight, change_height в классе Parrot.
В случае не передачи параметра - вес изменяется на 0.05
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

    def jump(self):
        print('Jump!')

    def birthday(self):
        self.age += 1

    def sleep(self):
        print('Sleep!')

    def change_weight(self, weight=0.2):
        self.weight += weight

    def change_height(self, height=0.2):
        self.height += height


class Dog(Pet):
    def bark(self):
        print('Bark!')


class Cat(Pet):
    def meow(self):
        print('Meow!')


class Parrot(Pet):
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
    not_my_parrot = Parrot('Lise', 5, 'Dima', 0.01, 1.5)
    not_my_parrot.fly()
    print(not_my_parrot.height)
    not_my_parrot.change_height()
    print(not_my_parrot.height)
    not_my_parrot.sleep()


if __name__ == '__main__':
    main()
