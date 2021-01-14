"""
Создать csv файл с данными о ежедневной погоде.
Структура:  Дата, Место, Градусы, Скорость ветра.
Найти среднюю погоду(скорость ветра и градусы) для Минск за последние 7 дней.
"""

from files.csv_utils import read, write


def create_file(my_file):
    title = ['Дата', 'Место', 'Градусы', 'Скорость ветра']
    info = [
        ['14 января', 'Минск', '-5', '6'],
        ['15 января', 'Минск', '-13', '5'],
        ['16 января', 'Минск', '-20', '4'],
        ['17 января', 'Минск', '-22', '4'],
        ['18 января', 'Минск', '-19', '3'],
        ['19 января', 'Минск', '-18', '4'],
        ['20 января', 'Минск', '-5', '4']
    ]
    write(my_file, title, info)


def average_weather_week(my_file):
    average = 0
    title, info = read(my_file)
    for i, degrees in enumerate(info):
        average += int(degrees[2])
    average /= 7
    return average


def main():
    file = 'files_11.csv'
    create_file(file)
    pr_average = average_weather_week(file)
    print(f'Средняя температа в Минска, за последние 7 дней равна: '
          f'{pr_average}')


if __name__ == '__main__':
    main()
