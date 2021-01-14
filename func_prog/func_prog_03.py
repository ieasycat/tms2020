"""
Дан список словарей.
Каждый словарь описывает машину(серийный номер и год выпуска).
Создать новый список со всеми машинами, год выпуска которых больше n
"""


def main():
    cars = [
        {
            'numbers': 1234,
            'years': 2008
        },
        {
            'numbers': 4567,
            'years': 2010
        },
        {
            'numbers': 7890,
            'years': 2021
        }
    ]
    n = 2009
    new_cars = [car for car in cars if car['years'] > n]
    print(new_cars)


if __name__ == '__main__':
    main()
