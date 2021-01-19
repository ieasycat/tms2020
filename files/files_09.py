"""
Использовать результаты files_08. Все функции описываются в csv_utils.py.
Проверка работы функции осуществляется в files_09.py.
Создать функцию подсчета полной суммы всех товаров.
Создать функцию поиска самого дорогого товара.
Создать функцию самого дешевого товара.
Создать функцию уменьшения количества товара(на n, по-умолчанию на 1)
"""
from files import csv_utils


def main():
    source_file = 'files_08.csv'
    main_file = 'files_09.csv'
    title, info_product = csv_utils.read(source_file)
    csv_utils.write(main_file, title, info_product)
    title, info_product = csv_utils.read(main_file)
    pr_summ = csv_utils.my_summ(info_product)
    pr_expensive = csv_utils.expensive(info_product)
    pr_cheap = csv_utils.cheap(info_product)
    csv_utils.decrease(main_file, 2, 100)
    print(f'Общая сумма товаров - {pr_summ}')
    print(f'Самый дорогой товар - {pr_expensive}')
    print(f'Самый дешевый товар - {pr_cheap}')


if __name__ == '__main__':
    main()
