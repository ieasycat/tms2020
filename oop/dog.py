class Dog:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def bark(self):
        print('Woof Woof!')

    def run(self):
        print('Run!')

    def jump(self):
        print('Jump!')


def main():
    dog = Dog('Bobik', 2, 2, 25)
    new_dog = Dog('Bager', 1.5, 1.5, 15)
    print(dog, new_dog)
    dog.bark()
    dog.run()
    dog.jump()
    dog_1 = Dog('Arni', 3, 1, 20)
    print(f'Name Dog: {dog_1.name}')
    print(f'Age Dog: {dog_1.age}')
    print(f'Height Dog: {dog_1.height}')
    print(f'Weight Dog: {dog_1.weight}')


if __name__ == '__main__':
    main()
