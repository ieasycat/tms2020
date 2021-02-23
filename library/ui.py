from library.buisness_logic import \
    create_book, read_books, update_book, del_book, filter_books, MyException
from library.book import Books, session


def display_books():
    books = read_books()
    for book in books:
        print(book)
    print()


def crete_books():
    title = input('Введите название книги: ')

    check = session.query(Books.title).filter_by(title=title)

    for book in check:
        pass
    if title in book.title:
        print('Данная книга уже есть.')
    else:
        pages = int(input('Введите кол-во страниц в книге: '))
        author = input('Введите имя автора книги: ')
        price = float(input('Введите ценну книги: '))
        release_year = int(input('Введите год издания книги: '))
        create_book({'title': title,
                     'pages': pages,
                     'author': author,
                     'price': price,
                     'release_year': release_year})
    print()


def change_book():
    book_id = int(input('Введите ID книги, которую хотите изменить: '))
    my_title = input('Введите название книги: ') \
        or Books.title

    check = session.query(Books.title).filter_by(title=my_title)

    for book in check:
        pass
    if my_title in book.title:
        print('Данная книга уже есть.')
    else:
        my_pages = input('Введите кол-во страниц в книге: ') \
                   or Books.pages
        my_author = input('Введите имя автора книги: ') \
            or Books.author
        my_price = input('Введите ценну книги: ') \
            or Books.price
        my_release_year = input('Введите год издания книги: ') \
            or Books.release_year
        update_book(book_id, {'title': my_title, 'pages': my_pages,
                              'author': my_author, 'price': my_price,
                              'release_year': my_release_year})
    print()


def del_books():
    book_id = int(
        input('Введите ID колонки, которую хотите удалить: '))
    del_book(book_id)
    print()


def filters_books():
    author = input('Введите имя автора: ')
    print()
    filters = filter_books(author)
    if len(list(filters)) > 0:
        for my_filter in filters:
            print(my_filter)
    else:
        print('Такого автора нет.')
    print()


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
            display_books()
        elif count == 2:
            crete_books()
        elif count == 3:
            change_book()
        elif count == 4:
            del_books()
        elif count == 5:
            filters_books()
        elif count == 0:
            print('Выход')
            break

        else:
            raise MyException


def main():
    pass


if __name__ == '__main__':
    main()
