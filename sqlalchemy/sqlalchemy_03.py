"""
Создать файл sqlalchemy_03.py.
Написать программу: пользователь вводит год.
Отобразить на экране те книги, год которых меньше
введенного пользователем года.
Если таких книг нет - вывести сообщение: Not found.
Для проверки количества записей - привести
результат запроса к списку и использовать функцию len()
"""

from sqlalchemy import create_engine

year = int(input('Введите год книги: '))
my = create_engine('sqlite:///sa_test.db')

result = my.execute(f"""
    select * from Book
    where {year} < release_year
""")

books = list(result)
if len(books) > 0:
    for book in books:
        print(book)
else:
    print('Not found')
