"""
Создать файл book.py.
Создать класс Book.
Атрибуты: количество страниц, год издания, автор, цена.
Добавить валидацию в конструкторе на ввод корректных данных.
Создать иерархию ошибок.
Ошибки вызываются при попытке создания не правильного объекта.
"""
from datetime import datetime


class Book:
    def __init__(self, number_of_pages, year_of_publication, author, price):
        self.number_of_pages = number_of_pages
        self.year_of_publication = year_of_publication
        self.author = author
        self.price = price
        now = datetime.now()
        if self.number_of_pages <= 0:
            raise ErrorInThePage
        if self.year_of_publication > now.year:
            raise ErrorInTheYear
        if self.author == '':
            raise ErrorInTheAuthor
        if self.price < 0:
            raise ErrorInThePrice

    def __str__(self):
        return f'{self.number_of_pages}, ' \
                f'{self.year_of_publication}, ' \
                f'{self.author}, ' \
                f'{self.price}'


class ErrorInThePage(Exception):
    def __init__(self, message='Страница не может быть отрицательной!'):
        super(ErrorInThePage, self).__init__(message)


class ErrorInTheYear(Exception):
    def __init__(self, message='Год издания не может быть в будущем!'):
        super(ErrorInTheYear, self).__init__(message)


class ErrorInTheAuthor(Exception):
    def __init__(self, message='Строка автора не может быть пустой!'):
        super(ErrorInTheAuthor, self).__init__(message)


class ErrorInThePrice(Exception):
    def __init__(self, message='Цена не может быть отрицательной!'):
        super(ErrorInThePrice, self).__init__(message)


def main():
    my_book = Book(1, 1992, 'Anton', 500)
    print(my_book)


if __name__ == '__main__':
    main()
