"""
Создать универсальный декоратор,
который меняет порядок аргументов в функции на противоположный.
"""

from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args = (args[0][::-1])
        result = func(args, **kwargs)
        return result
    return wrapper


@my_decorator
def my_funcs(words):
    return words


def main():
    my_words = ['Ася', 'Python', 'World', 'Бывает']
    pr = my_funcs(my_words)
    print(pr)


if __name__ == '__main__':
    main()
