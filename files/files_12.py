"""
Дан файл, содержащий различные даты.
Каждая дата - это число, месяц и год. Найти самую раннюю дату. [02-8.1-ML-29]
"""

from files.csv_utils import write, read
from datetime import date


def create_file(mt_file):
    title = ['Дата']
    dates = [
        [date(2019, 9, 25)],
        [date(2020, 12, 5)],
        [date(1992, 8, 11)],
        [date(2021, 1, 10)],
        [date(2001, 10, 31)],
        [date(1999, 5, 1)],
        [date(2011, 4, 13)]
    ]
    write(mt_file, title, dates)


def search(my_file):
    title, date = read(my_file)
    old_date = date[0]
    for i in date:
        if old_date > i:
            old_date = i
    old_date = ''.join(old_date)
    return old_date


def main():
    file = 'files_12.csv'
    create_file(file)
    pr = search(file)
    print(pr)


if __name__ == '__main__':
    main()
