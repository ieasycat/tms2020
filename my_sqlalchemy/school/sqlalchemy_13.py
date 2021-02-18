"""
Описать модель Книга(Book) с помощью sqlalchemy в файле models.py.
Книга характеризуется названием,
количеством страниц и студентами у которых эта книга.
Создать файл sqlalchemy_13.py. Создать 5 книг.
Получить всех студентов и добавить каждому студенту эти пять книг.
"""

from my_sqlalchemy.school.models import Book, Student, session

students = session.query(Student).all()

book = Book(title='Harry Potter', pages=789, students=students)
book_2 = Book(title='Harry Potter 2 ', pages=981, students=students)
book_3 = Book(title='Harry Potter 3', pages=750, students=students)
book_4 = Book(title='Harry Potter 4', pages=814, students=students)
book_5 = Book(title='Harry Potter 5', pages=801, students=students)
session.add_all([book, book_2, book_3, book_4, book_5])
session.commit()
