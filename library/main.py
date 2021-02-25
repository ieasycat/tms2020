"""
Создать ветку library от master.
Создать ветку library_solution от ветки library.Создать пакет library.
Написать программу с пользовательским интерфейсом.
Программа реализует CRUD для работы с книгами.
Также программа позволяет фильтровать книги по автору.
Реализовать программу в виде раздельных модулей
(class.py, buisness_logic.py, ui.py, main.py).
Сделать пул реквест из ветки library_solution в library
"""

from library.ui import functionality


def main():
    functionality()


if __name__ == '__main__':
    main()
