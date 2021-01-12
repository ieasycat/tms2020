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


def main():
    read()
    write()
    add()
    dell()


if __name__ == '__main__':
    main()
