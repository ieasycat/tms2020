"""
Создать файл sqlalchemy_07.py.
Получить все книги и вывести их на экран в формате
год - название - автор.
"""

from my_sqlalchemy.book import Books, session

books = session.query(Books)
for i in books:
    print(f'{i.release_year} - {i.title} - {i.author}')
