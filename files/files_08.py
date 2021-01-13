"""
В файле files_08 импортировать функции.
С помощью функций создать файл с информацией о товарах
(Имя товара, цена, количество, комментарий).
Прочесть файл, Добавить новую позицию в конец. Удалить третью строку.
"""

from files import csv_utils


def create_file(file):
    title = ['Имя товара', 'цена', 'количество', 'комментарий']
    info_product = [
        ['Ручка', '15', '50', 'гелевая синего цвета'],
        ['Тетрадь в клетку', '30', '200', 'в мелкую клетку'],
        ['Ластик', '50', '700', 'твердый']
    ]
    csv_utils.write(file, title, info_product)


def new_poz(text):
    new_product = ['Замазка', '80', '500', '500мл']
    csv_utils.add(text, new_product)


def dell_poz(text):
    csv_utils.dell(text, 3)


def main():
    file = 'files_08.csv'
    create_file(file)
    name, info = csv_utils.read(file)
    print(f'Заголовок - {name}')
    print(f'Информация - {info}')
    new_poz(file)
    dell_poz(file)


if __name__ == '__main__':
    main()
