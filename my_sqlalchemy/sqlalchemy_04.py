"""
Создать файл sqlalchemy_04.py.
Написать программу: пользователь вводит данные о книге.
Пользователю отображается введенная им информация.
Пользователю задается вопрос: “Хотите сохранить эту книгу?”.
Если ответ да - выполнить метод .commit(), иначе - .rollback()
"""

from sqlalchemy import create_engine


def create_db(title, pages, author):
    my_db = create_engine('sqlite:///my_book.db')
    my_db.execute("""
        create table Book (
            id integer primary key,
            title varchar,
            pages int,
            author varchar
            );
    """)

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

    result = conn.execute("""select * from Book""")
    for book in result:
        print(book)

    voice = (input('Сохранить? ')).lower()
    if 'да' or 'yes' in voice:
        trans.commit()
    else:
        conn.close()


def main():
    title = input('Введите название книги: ')
    pages = int(input('Введите количество страниц: '))
    author = input('Введите автора: ')
    create_db(title, pages, author)


if __name__ == '__main__':
    main()
