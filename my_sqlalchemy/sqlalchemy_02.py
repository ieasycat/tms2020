"""
Создать файл sqlalchemy_02.py.
Создать соединение к базе sa_test.db.
Создать 5 книг с помощью my_sqlalchemy.
"""

from sqlalchemy import create_engine

my = create_engine('sqlite:///sa_test.db')

my.execute("""
    insert into Book (
        title,
        pages,
        author,
        price,
        release_year)
    values
    ('Harry Potter', 999, 'Diana', 709, 2008),
    ('Harry Potter 2', 809, 'Diana', 699.10, 2010),
    ('Harry Potter 3', 750, 'Diana', 650.70, 2012),
    ('Harry Potter 4', 890, 'Diana', 700.11, 2014),
    ('Harry Potter 5', 705, 'Diana', 630.36, 2016);
""")
