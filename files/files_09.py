"""
Использовать результаты files_08. Все функции описываются в csv_utils.py.
Проверка работы функции осуществляется в files_09.py.
Создать функцию подсчета полной суммы всех товаров.
Создать функцию поиска самого дорогого товара.
Создать функцию самого дешевого товара.
Создать функцию уменьшения количества товара(на n, по-умолчанию на 1)
"""
from files import csv_utils


def open_file(old_file):
    title, info_product = csv_utils.read(old_file)
    return title, info_product


def write_new_file(new_file, fields, row):
    csv_utils.write(new_file, fields, row)
    title, info_product = csv_utils.read(new_file)
    return title, info_product


def my_summ(info):
    summ = 0
    for i, number in enumerate(info):
        tmp = int(info[i][1])
        summ += tmp
    return summ


def expensive(info):
    max = 0
    for i, number in enumerate(info):
        tmp = int(info[i][1])
        if max < tmp:
            max = tmp
    max = str(max)
    for i, k in enumerate(info):
        if max in info[i][1]:
            return info[i][0]


def cheap(info):
    my_min = int(info[0][1])
    for i, number in enumerate(info):
        tmp = int(info[i][1])
        if my_min > tmp:
            my_min = tmp
    my_min = str(my_min)
    for i, k in enumerate(info):
        if my_min in info[i][1]:
            return info[i][0]


def decrease(file, product, n=1):
    title, info_product = open_file(file)
    for i, numbers in enumerate(info_product):
        if i == product:
            info_product[i][2] = int(info_product[i][2]) - n
    write_new_file(file, title, info_product)


def main():
    source_file = 'files_08.csv'
    main_file = 'files_09.csv'
    title, info_product = open_file(source_file)
    write_new_file(main_file, title, info_product)
    title, info_product = open_file(main_file)
    pr_summ = my_summ(info_product)
    pr_expensive = expensive(info_product)
    pr_cheap = cheap(info_product)
    decrease(main_file, 2, 100)
    print(f'Общая сумма товаров - {pr_summ}')
    print(f'Самый дорогой товар - {pr_expensive}')
    print(f'Самый дешевый товар - {pr_cheap}')


if __name__ == '__main__':
    main()
