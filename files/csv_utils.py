"""
Написать функции по работе с csv файлами в файле csv_utils.py.
Чтение. Запись. Добавление записи(по позиции, по-умолчанию в конец).
Удаление записи(по позиции, по-умолчанию последнюю).
"""

import csv


def read(text):
    rows = []
    with open(text) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            rows.append(row)
        fields = rows[0]
        data = rows[1:]
    return fields, data


def write(text, fields, row):
    with open(text, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(fields)
        csv_writer.writerows(row)
    return csv_writer


def add(text, row, place=-1):
    fields, data = read(text)
    if place == -1:
        data.append(row)
    else:
        data.insert(place - 1, row)
    write(text, fields, data)


def dell(text, place=-1):
    fields, data = read(text)
    if place == -1:
        data.pop()
    else:
        data.pop(place - 1)
    write(text, fields, data)


def my_summ(info):
    summ = 0
    for i, number in enumerate(info):
        tmp = int(info[i][1]) * int(info[i][2])
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
    title, info_product = read(file)
    for i, numbers in enumerate(info_product):
        if i == product:
            info_product[i][2] = int(info_product[i][2]) - n
    write(file, title, info_product)


def main():
    read()
    write()
    add()
    dell()
    my_summ()
    expensive()
    cheap()
    decrease()


if __name__ == '__main__':
    main()
