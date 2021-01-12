"""
Написать функции по работе с csv файлами в файле csv_utils.py.
Чтение. Запись. Добавление записи(по позиции, по-умолчанию в конец).
Удаление записи(по позиции, по-умолчанию последнюю).
"""

import csv


def read(file):
    rows = []
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            rows.append(row)
        fields = rows[0]
        data = rows[1:]
    return fields, data


def write(file, fields, row):
    with open(file, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(fields)
        csv_writer.writerows(row)
    return csv_writer


def add(file, row, place=-1):
    fields, data = read(file)
    if place == -1:
        data.append(row)
    else:
        data.insert(place - 1, row)
    write(file, fields, data)


def dell(file, place=-1):
    fields, data = read(file)
    if place == -1:
        data.pop()
    else:
        data.pop(place - 1)
    write(file, fields, data)


def main():
    add('text.txt', ['allo', 'mmm'], 2)


if __name__ == '__main__':
    main()
