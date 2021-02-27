from sqlalchemy_utils import create_database, database_exists
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey

DB_USER = 'postgres'
DB_PASS = 'postgres'
DB_NAME = 'Cars'
DB_ECHO = True

engine = create_engine(
    f'postgresql://{DB_USER}:{DB_PASS}@localhost/{DB_NAME}',
)

if not database_exists(engine.url):
    create_database(engine.url)

Base = declarative_base()


class Brand(Base):
    __tablename__ = 'brand'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __str__(self):
        return f'ID: {self.id}, brand: {self.name}'


class Car(Base):
    __tablename__ = 'car'
    id = Column(Integer, primary_key=True)
    model = Column(String)
    release_year = Column(Integer)
    brand_id = Column(
        Integer,
        ForeignKey('brand.id'),
        nullable=False,
    )
    brand = relationship(
        'Brand',
        foreign_keys='Car.brand_id',
        backref='cars'
    )

    def __str__(self):
        return f'ID: {self.id}, model: {self.model}, ' \
               f'release_year: {self.release_year}, ' \
               f'brand: {self.brand}'


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
