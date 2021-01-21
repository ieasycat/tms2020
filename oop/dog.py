class Dog:
    def bark(self):
        print('Woof Woof!')

    def run(self):
        print('Run!')

    def jump(self):
        print('Jump!')

    def __init__(self, name, age, height, weight, master, address='Minsk'):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.__master = master
        self.__address = address

    def change_name(self, name):
        self.name = name

    def get_master(self):
        return self.__master

    def get_address(self):
        return self.__address

    def set_address(self, address):
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
    # oop_04
    dog_1 = Dog('Arni', 3, 1, 20, "I'm")
    print(f'Name Dog: {dog_1.name}')
    print(f'Age Dog: {dog_1.age}')
    print(f'Height Dog: {dog_1.height}')
    print(f'Weight Dog: {dog_1.weight}')
    # oop_05
    print(f'Name Dog: {dog_1.name}')
    dog_1.change_name('Big Arni')
    print(f'Name Dog: {dog_1.name}')
    # oop_06
    print(f'Master Dog: {dog_1.get_master()}')
    # oop_07
    print(f'Address Dog: {dog_1.get_address()}')
    dog_1.set_address('London')
    print(f'Address Dog: {dog_1.get_address()}')


if __name__ == '__main__':
    main()
