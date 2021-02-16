"""
Создать пакет school.
Создать базу school в postgre.
Создать файл models.py.
Создать таблицу Учебной группы(Group)
с помощью sqlalchemy в декларативном стиле.
Группа характеризуется названием(name).
"""
from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

DB_USER = 'postgres'
DB_PASS = 'postgres'
DB_NAME = 'school'

engine = create_engine(
    f'postgresql://{DB_USER}:{DB_PASS}@localhost/{DB_NAME}',
    echo=True,
)

if not database_exists(engine.url):
    create_database(engine.url)

Base = declarative_base()


class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name


Base.metadata.create_all(engine)
