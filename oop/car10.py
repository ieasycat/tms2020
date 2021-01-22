"""
Создать файл car10.py.
Создать класс Car.
Атрибуты: марка, модель, год  выпуска, скорость(по умолчанию 0).
Методы: увеличить скорости(скорость + 5), уменьшение скорости(скорость  - 5),
стоп(сброс скорости на 0), отображение скорости,
разворот(изменение знака скорости). Все атрибуты приватные.
"""


class Car:
    def __init__(self, make, model, years, speed=0):
        self.__make = make
        self.__model = model
        self.__years = years
        self.__speed = speed

    @property
    def speed(self):
        return self.__speed

    def speed_increase(self):
        self.__speed += 5

    def speed_reduction(self):
        self.__speed -= 5

    def speed_reset(self):
        self.__speed = 0

    def speed_reversal(self):
        self.__speed *= -1


def main():
    car_1 = Car('Opel', 'Tigra B', 1996)
    print(car_1.speed)
    car_1.speed_increase()
    print(car_1.speed)
    car_1.speed_reduction()
    print(car_1.speed)
    car_1 = Car('Opel', 'Tigra B', 1996, 10)
    print(car_1.speed)
    car_1.speed_reset()
    print(car_1.speed)
    car_1.speed_reduction()
    print(car_1.speed)
    car_1.speed_reversal()
    print(car_1.speed)


if __name__ == '__main__':
    main()
