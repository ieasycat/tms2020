"""
Добавить два новых атрибута в родительский класс: weight и height.
Добавить методы change_weight, change_height принимающий один параметр
и прибавляющий его к соответствующему аргументу.
В случае если параметр не был передан, увеличивать на 0.2.
Изменить метод fly класса Parrot. Если вес больше 0.1
выводить сообщение This parrot cannot fly.

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
    my_cat = Cat('Barsik', 10, 'Anton', 5, 2)
    print(my_cat.height)
    my_cat.change_height(1)
    print(my_cat.height)
    my_cat.change_height()
    print(my_cat.height)
    my_cat.run()
    my_cat.meow()
    my_dog = Dog('Alex', 3, 'Alex', 9, 4)
    my_dog.run()
    my_dog.jump()
    my_dog.bark()
    not_my_parrot = Parrot('Lise', 5, 'Dima', 0.01, 1.5)
    not_my_parrot.fly()
    print(not_my_parrot.height)
    not_my_parrot.change_height()
    print(not_my_parrot.height)
    not_my_parrot.sleep()


if __name__ == '__main__':
    main()
