"""
Создать файл sqlalchemy_08.py.
Написать программу: пользователь вводит границы фильтрации по году.
Отобразить на экране те книги, год которых находиться в заданных границах.
Если таких книг нет - вывести сообщение: Not found.
"""

from sqlalchemy import and_

from my_sqlalchemy.book import Books, session

one = int(input('Введите с какого года начать фильтрацию: '))
two = int(input('Введите по какой года закончить фильтрацию: '))

books = session.query(Books).filter(and_(Books.release_year >= one,
                                         Books.release_year <= two)).all()
if books:
    for book in books:
        print(f'Title book: {book.title}, '
              f'pages book: {book.pages}, '
              f'author book: {book.author}, '
              f'price book: {book.price}, '
              f'release year book: {book.release_year}')
else:
    print('Not found!')
