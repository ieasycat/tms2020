"""
Создать файл time.py.
Создать класс MyTime.
Атрибуты: hours, minutes, seconds.
Переопределить магические методы сравнения(равно, не равно),
сложения, вычитания, вывод на экран.
Перегрузить конструктор на обработку входных параметров вида:
одна строка, три числа, другой объект класса MyTime.
В остальных случаях создавать объект по-умолчанию(0-0-0)
"""


class MyTime:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __eq__(self, other):
        return all(
            [self.hours == other.hours,
             self.minutes == other.minutes,
             self.seconds == other.seconds]
        )

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        new_hours = self.hours + other.hours
        new_minutes = self.minutes + other.minutes
        new_seconds = self.seconds + other.seconds
        return f'{new_hours}-{new_minutes}-{new_seconds}'

    def __sub__(self, other):
        new_hours = self.hours - other.hours
        new_minutes = self.minutes - other.minutes
        new_seconds = self.seconds - other.seconds
        return f'{new_hours}-{new_minutes}-{new_seconds}'

    def __str__(self):
        return f'{self.hours}-{self.minutes}-{self.seconds}'

    def reset(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0


def main():
    time_one = MyTime(15, 20, 30)
    time_two = MyTime(0, 1, 5)

    print(time_one)
    print(time_two)

    print(time_one + time_two)
    print(time_one - time_two)


if __name__ == '__main__':
    main()
