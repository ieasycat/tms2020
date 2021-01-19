"""
Дан файл, содержащий различные даты.
Каждая дата - это число, месяц и год. Найти самую раннюю дату. [02-8.1-ML-29]
"""

from files.csv_utils import read
from datetime import datetime


def search(my_file):
    title, dates = read(my_file)
    datetime_object = []
    for i in dates:
        datetime_object.append(datetime.strptime(i[0], '%d.%m.%Y'))
    old_date = datetime_object[0]
    for i in datetime_object:
        if old_date > i:
            old_date = i
    return old_date.strftime('%d.%m.%Y')


def main():
    file = 'files_12.csv'
    pr = search(file)
    print(pr)


if __name__ == '__main__':
    main()
