"""
Написать декоратор, который будет выводить время выполнения функции
from datetime import datetime
time = datetime.now()
"""

from datetime import datetime
from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        old_time = datetime.now()
        result = func(*args, **kwargs)
        new_time = datetime.now()
        print(new_time - old_time)
        return result
    return wrapper


@my_decorator
def my_func(a, b):
    x1 = a + b
    x2 = a * b
    x3 = b / a
    x4 = b - a
    return x1, x2, x3, x4


def main():
    my_func(10, 40)


if __name__ == '__main__':
    main()
