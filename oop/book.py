class Book:
    def __init__(self, number_of_pages, year_of_publication, author, price):
        self.number_of_pages = number_of_pages
        self.year_of_publication = year_of_publication
        self.author = author
        self.price = price

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
    number_of_pages = int(input('Введите количество страниц в книге: '))
    if number_of_pages < 0:
        raise ErrorInThePage
    year_of_publication = int(input('Введите год издания книги: '))
    if year_of_publication > 2021:
        raise ErrorInTheYear
    author = input('Введите автора книги: ')
    if author == '':
        raise ErrorInTheAuthor
    price = int(input('Введите цену книги: '))
    if price < 0:
        raise ErrorInThePrice
    my_book = Book(number_of_pages,
                   year_of_publication,
                   author,
                   price)
    print(my_book)


if __name__ == '__main__':
    main()
