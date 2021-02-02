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
    def __init__(self, *args):
        if len(args) > 1 and type(args[0]) == int:
            self.hours = args[0]
            self.minutes = args[1]
            self.seconds = args[2]
        elif len(args) == 1 and type(args[0]) == int:
            self.hours = 0
            self.minutes = 0
            self.seconds = args[0]
        elif len(args) >= 1 and type(args[0]) == str:
            time = args[0].split('-')
            self.hours = int(time[0])
            self.minutes = int(time[1])
            self.seconds = int(time[2])
        elif len(args) >= 1 and type(args[0]) == MyTime:
            self.hours = args[0].hours
            self.minutes = args[0].minutes
            self.seconds = args[0].seconds
        else:
            self.hours = 0
            self.minutes = 0
            self.seconds = 0
        self.hours, self.minutes, self.seconds = \
            MyTime.conversion(self.hours, self.minutes, self.seconds)

    @staticmethod
    def conversion(hours, minutes, seconds):
        if seconds > 59:
            minutes += round(seconds / 60)
            seconds %= 60
        if minutes > 59:
            hours += round(minutes / 60)
            minutes %= 60
        if hours > 24:
            hours -= 24
        return hours, minutes, seconds

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
        new_hours, new_minutes, new_seconds = \
            MyTime.conversion(new_hours, new_minutes, new_seconds)
        return f'{new_hours}-{new_minutes}-{new_seconds}'

    def __sub__(self, other):
        new_hours = self.hours - other.hours
        new_minutes = self.minutes - other.minutes
        new_seconds = self.seconds - other.seconds
        new_hours, new_minutes, new_seconds = \
            MyTime.conversion(new_hours, new_minutes, new_seconds)
        if new_hours < 0:
            new_hours *= -1
        if new_minutes < 0:
            new_minutes *= -1
        if new_seconds < 0:
            new_seconds *= -1
        if self.hours < other.hours:
            new_hours = 24 - new_hours
        if self.minutes < other.minutes:
            new_minutes = 60 - new_minutes
        if self.seconds < other.seconds:
            new_seconds = 60 - new_seconds
        return f'{new_hours}-{new_minutes}-{new_seconds}'

    def __str__(self):
        hours, minutes, seconds = \
            MyTime.conversion(self.hours, self.minutes, self.seconds)
        return f'{hours}-{minutes}-{seconds}'

    def reset(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0


def main():
    time_one = MyTime(23, 10, 10)
    time_two = MyTime('15-23-31')
    time_three = MyTime(time_two)
    time_four = MyTime()

    print(f"This's One Time - {time_one}")
    print(f"This's Two Time - {time_two}")
    print(f"This's Three Time - {time_three}")
    print(f"This's Four Time - {time_four}")

    print(f"This's sum one and two time - {time_one + time_two}")
    print(f"This's sum one and three time - {time_one + time_three}")
    print(f"This's sub one and two time - {time_one - time_two}")
    print(f"This's sub one and three time - {time_one - time_three}")
    print(f"This's sub one four time - {time_one - time_four}")

    print(f"This's eq one and two time - {time_one == time_two}")
    print(f"This's eq one and three time - {time_one == time_three}")
    print(f"This's eq one and four time - {time_one == time_four}")
    print(f"This's ne one and two time - {time_one != time_two}")
    print(f"This's ne one and three time - {time_one != time_three}")
    print(f"This's ne one and four time - {time_one != time_four}")


if __name__ == '__main__':
    main()
