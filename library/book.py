from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Books(Base):
    __tablename__ = 'Book'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    pages = Column(Integer)
    author = Column(String)
    price = Column(Float)
    release_year = Column(Integer)

    def __init__(self, title, pages, author, price, release_year):
        self.title = title
        self.pages = pages
        self.author = author
        self.price = price
        self.release_year = release_year

    def __str__(self):
        return f'ID: {self.id}, title: {self.title}, ' \
               f'pages: {self.pages}, author: {self.author}, ' \
               f'price: {self.price}, release_year: {self.release_year}'


my_db = create_engine('sqlite:///books.db')
Base.metadata.create_all(my_db)
Session = sessionmaker(bind=my_db)
session = Session()
