"""
Создать файл book.py.
Создать базу book.db.
Создать таблицу Book с помощью механизма описания таблиц my_sqlalchemy.
Атрибуты: id(integer primary key), title(varchar), pages(int),
author(varchar), price(float), release_year(int)
"""

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, Float

engine = create_engine('sqlite:///book.db', echo=True)
metadata = MetaData()
my_table = Table('Book', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('title', String),
                 Column('pages', Integer),
                 Column('author', String),
                 Column('price', Float),
                 Column('release_year', Integer),
                 )
metadata.create_all(engine)
