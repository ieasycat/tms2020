from sqlalchemy import Table, Column, Integer, String, MetaData, Float
from sqlalchemy import create_engine
from sqlalchemy.orm import mapper, sessionmaker

e = create_engine('sqlite:///book.db', echo=True)
metadata = MetaData()
book_table = Table('Book', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('title', String),
                   Column('pages', Integer),
                   Column('author', String),
                   Column('price', Float),
                   Column('release_year', Integer),
                   )
metadata.create_all(e)


class Books:
    def __init__(self, title, pages, author, price, release_year):
        self.title = title
        self.pages = pages
        self.author = author
        self.price = price
        self.release_year = release_year


mapper(Books, book_table)
Session = sessionmaker(bind=e)
session = Session()
