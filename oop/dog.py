class Dog:
    def bark(self):
        print('Woof Woof!')

    def run(self):
        print('Run!')

    def jump(self):
        print('Jump!')

    def __init__(self, name, age, height, weight, master, address='Minsk'):
        self.__name = name
        self.__age = age
        self.__height = height
        self.__weight = weight
        self.__master = master
        self.__address = address

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @property
    def master(self):
        return self.__master

    @master.setter
    def master(self, master):
        self.__master = master

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address


def main():
    # oop_02
    dog = Dog('Bobik', 2, 2, 25, "I'm", 'Minsk')
    new_dog = Dog('Bager', 1.5, 1.5, 15, "I'm", 'Minsk')
    print(dog, new_dog)
    # oop_03
    dog.bark()
    dog.run()
    dog.jump()
    dog_1 = Dog('Arni', 3, 1, 20, "I'm")
    # oop_08
    print(dog_1.name)
    dog_1.name = 'Big Arni'
    print(dog_1.name)


if __name__ == '__main__':
    main()
