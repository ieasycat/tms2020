from library.book import Books, session


def create_book(title, pages, author, price, release_year):
    book = Books(title, pages, author, price, release_year)
    session.add(book)
    session.commit()


def read_books():
    books = session.query(Books).all()
    return books


def update_book(book_id, new_values):
    book = session.query(Books).filter(Books.id == book_id).first()
    book.title = new_values['title']
    book.pages = new_values['pages']
    book.author = new_values['author']
    book.price = new_values['price']
    book.release_year = new_values['release_year']
    session.add(book)
    session.commit()


def del_book(book_id):
    session.query(Books).filter(Books.id == book_id).delete()
    session.commit()


def filter_books(filter_author):
    filters = session.query(Books).filter_by(author=filter_author)
    return filters


def main():
    pass


if __name__ == '__main__':
    main()
