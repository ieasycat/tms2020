"""
Создать универсальный декоратор,
который меняет порядок аргументов в функции на противоположный.
"""

from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        kwargs = {key: value[::-1] for key, value in kwargs.items()}
        result = func((*args[::-1], kwargs))
        return result
    return wrapper


@my_decorator
def my_funcs(words):
    return words


def main():
    pr = my_funcs('Ася', 'Python', 'World', 'Бывает', a='Test', b='Trash')
    print(pr)


if __name__ == '__main__':
    main()
