"""
Создать список поездов. Структура словаря: номер поезда,
пункт и время прибытия, пункт и время отбытия.
Вывести все сведения о поездах,
время пребывания в пути которых превышает 7 часов 20 минут.[02-7.3-ML02]
Примечание: данное задание подразумевает самостоятельное
изучение принципов работы со временем в Python(библиотека datetime)
"""

# Из-за этого flake8, который ругаетсян на длинну, надо делать переменные ;(

from datetime import timedelta


def calculation_trains(trains):
    for train in trains:
        a = train['arrival time']
        b = train['departure time']
        if a - b > timedelta(hours=7, minutes=20):
            print(f"Номер поезда: {train['number']}, "
                  f"следует: {train['p_departure']} - {train['p_arrival']}, "
                  f"время отправления: {b}, "
                  f"время прибытия {a}")
            print(f"Время в пути - {a - b}")
        print()


def main():
    trains_listt = [
        {
            'number': '140-139',
            'p_arrival': 'Москва',
            'arrival time': timedelta(hours=19, minutes=50),
            'p_departure': 'Минск',
            'departure time': timedelta(hours=10, minutes=5),
        },
        {
            'number': '140-252',
            'p_arrival': 'Гродно',
            'arrival time': timedelta(hours=14, minutes=50),
            'p_departure': 'Минск',
            'departure time': timedelta(hours=9, minutes=35),
        },
        {
            'number': '10-115',
            'p_arrival': 'Орша',
            'arrival time': timedelta(hours=20, minutes=5),
            'p_departure': 'Брест',
            'departure time': timedelta(hours=7, minutes=35),
        },
    ]
    calculation_trains(trains_listt)


if __name__ == '__main__':
    main()
