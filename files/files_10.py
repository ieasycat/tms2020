"""
Создать csv файл с данными следующей структуры: Имя, Фамилия, Возраст.
Создать отчетный файл с информацией по количеству людей входящих в ту
или иную возрастную группу. Возрастные группы: 1-12, 13-18, 19-25, 26-40, 40+.
"""

from files.csv_utils import write, read


def create_file(file):
    title = ['Имя', 'Фамилия', 'Возраст']
    info = [
        ['Антон', 'Клименко', '28'],
        ['Никита', 'Клименко', '25'],
        ['Соня', 'Клименко', '10'],
        ['Сергей', 'Быковский', '22']
    ]
    write(file, title, info)


def report(file, info):
    title = [
        'Возрастная группа 1-12',
        'Возрастная группа 13-18:',
        'Возрастная группа 19-25:',
        'Возрастная группа 26-40:',
        'Возрастная группа 40+:'
    ]
    count = [0, 0, 0, 0, 0]
    age_group = []
    for i, text in enumerate(info):
        age_group.append(info[i][2])
    for i in age_group:
        if 1 <= int(i) <= 12:
            count[0] += 1
        elif 13 <= int(i) <= 18:
            count[1] += 1
        elif 19 <= int(i) <= 25:
            count[2] += 1
        elif 26 <= int(i) <= 40:
            count[3] += 1
        else:
            count[4] += 1
    count = [str(i) for i in count]
    write(file, title, count)


def main():
    file = 'files_10.csv'
    report_file = 'files_new_10.csv'
    create_file(file)
    a, b = read(file)
    report(report_file, b)


if __name__ == '__main__':
    main()
