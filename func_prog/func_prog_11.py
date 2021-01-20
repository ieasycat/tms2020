"""
Создать декоратор для функции, которая принимает список чисел.
Декоратор должен производить предварительную проверку данных -
удалять все четные элементы из списка.
"""

from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper(my_number):
        for i in my_number:
            if i % 2 == 0:
                my_number.pop(my_number.index(i))
        result = func(my_number)
        return result
    return wrapper


@my_decorator
def numbers(numbers_list):
    return numbers_list


def main():
    number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    pr = numbers(number)
    print(pr)


if __name__ == '__main__':
    main()
