"""
Создать файл sqlalchemy_04.py.
Написать программу: пользователь вводит данные о книге.
Пользователю отображается введенная им информация.
Пользователю задается вопрос: “Хотите сохранить эту книгу?”.
Если ответ да - выполнить метод .commit(), иначе - .rollback()
"""

from sqlalchemy import create_engine


def create_db(title, pages, author):
    my_db = create_engine('sqlite:///book.db')
    conn = my_db.connect()
    trans = conn.begin()
    conn.execute(f"""
        insert into Book (
                title,
                pages,
                author)
        values
        ('{title}', {pages}, '{author}')
    """)

    result = conn.execute(f"""select * from Book where title = '{title}'""")
    for book in result:
        print(book)

    voice = (input('Сохранить? ')).lower()
    if 'да' in voice:
        trans.commit()
    else:
        trans.rollback()
    conn.close()


def main():
    title = input('Введите название книги: ')
    pages = int(input('Введите количество страниц: '))
    author = input('Введите автора: ')
    create_db(title, pages, author)


if __name__ == '__main__':
    main()
