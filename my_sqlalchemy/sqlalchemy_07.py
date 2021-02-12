"""
Создать файл sqlalchemy_07.py.
Получить все книги и вывести их на экран в формате
год - название - автор.
"""

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, Float
from sqlalchemy.orm import mapper, sessionmaker


class Books:
    def __init__(self, title, pages, author, price, release_year):
        self.title = title
        self.pages = pages
        self.author = author
        self.price = price
        self.release_year = release_year


def create_db():
    db = create_engine('sqlite:///books.db')
    metadata = MetaData()
    my_table = Table('Book', metadata,
                     Column('id', Integer, primary_key=True),
                     Column('title', String),
                     Column('pages', Integer),
                     Column('author', String),
                     Column('price', Float),
                     Column('release_year', Integer),
                     )
    metadata.create_all(db)

    mapper(Books, my_table)

    sessn = sessionmaker(bind=db)
    session = sessn()

    book_1 = Books('Harry Potter', 999, 'Diana', 790.99, 2008)
    book_2 = Books('Harry Potter 2', 850, 'Diana', 749.33, 2010)
    book_3 = Books('Harry Potter 3', 897, 'Diana', 767, 2012)
    session.add_all([book_1, book_2, book_3])
    session.commit()

    books = session.query(Books)
    for i in books:
        print(f'{i.release_year} - {i.title} - {i.author}')


def main():
    create_db()


if __name__ == '__main__':
    main()
