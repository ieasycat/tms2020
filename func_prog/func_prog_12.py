"""
Создать универсальный декоратор,
который меняет порядок аргументов в функции на противоположный.
"""

from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args = args[::-1]
        result = func(*args, **kwargs)
        return result
    return wrapper


@my_decorator
def my_funcs(*args):
    return args


def main():
    pr = my_funcs('Ася', 'Python', 'World', 'Бывает')
    print(pr)


if __name__ == '__main__':
    main()
