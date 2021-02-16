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
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker

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


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    group_id = Column(Integer,
                      ForeignKey('group.id'),
                      nullable=False,
                      )

    group = relationship(
        'Group',
        foreign_keys='Student.group_id',
        backref='students',
        )


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
