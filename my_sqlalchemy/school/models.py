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
from sqlalchemy.orm import relationship, sessionmaker, backref

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

    def __str__(self):
        return f'{self.id}, {self.firstname}, {self.lastname}, {self.group_id}'


class Diary(Base):
    __tablename__ = 'diary'
    id = Column(Integer, primary_key=True)
    average_score = Column(Integer)
    student_id = Column(
        Integer,
        ForeignKey('student.id'),
        nullable=False,
    )
    student = relationship(
        'Student',
        foreign_keys='Diary.student_id',
        backref=backref('diary', uselist=False)
    )

    def __str__(self):
        return f'{self.id}, {self.average_score}, {self.student_id}'


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
