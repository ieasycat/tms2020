from library.buisness_logic import\
    create_book, read_books, update_book, del_book, filter_books


class MyException(Exception):
    def __init__(self, message='Такого выбора нет!'):
        super(MyException, self).__init__(message)


def functionality():
    while True:
        print('Если хотите просмотреть таблицу, нажмите "1".\n'
              'Если хотите добавить запись в таблицу, нажмите "2".\n'
              'Если хотите изменить запись, нажмите "3".\n'
              'Если хотите удалить запись, нажмите "4".\n'
              'Если хотите отфильровать запись, нажмите "5".\n'
              'Если хотите выйти, нажмите "0".\n')
        count = int(input('Ваш выбор: '))
        if count == 1:
            read_books()
            print()

        elif count == 2:
            title = input('Введите название книги: ')
            pages = int(input('Введите кол-во страниц в книге: '))
            author = input('Введите имя автора книги: ')
            price = float(input('Введите ценну книги: '))
            release_year = int(input('Введите год издания книги: '))
            create_book(title, pages, author, price, release_year)
            print()

        elif count == 3:
            book_id = int(input('Введите ID книги, которую хотите изменить: '))
            my_title = input('Введите название книги: ')
            my_pages = int(input('Введите кол-во страниц в книге: '))
            my_author = input('Введите имя автора книги: ')
            my_price = float(input('Введите ценну книги: '))
            my_release_year = int(input('Введите год издания книги: '))
            update_book(book_id, {'title': my_title, 'pages': my_pages,
                                  'author': my_author, 'price': my_price,
                                  'release_year': my_release_year})
            print()

        elif count == 4:
            book_id = int(
                input('Введите ID колонки, которую хотите удалить: '))
            del_book(book_id)
            print()

        elif count == 5:
            author = input('Введите имя автора: ')
            filter_books(author)
            print()

        elif count == 0:
            print('Выход')
            break

        else:
            raise MyException


def main():
    pass


if __name__ == '__main__':
    main()
