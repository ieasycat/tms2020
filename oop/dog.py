class Dog:
    def bark(self):
        print('Woof Woof!')

    def run(self):
        print('Run!')

    def jump(self):
        print('Jump!')


def main():
    dog = Dog()
    new_dog = Dog()
    print(dog, new_dog)
    dog.bark()
    dog.run()
    dog.jump()


if __name__ == '__main__':
    main()
