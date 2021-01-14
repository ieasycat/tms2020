"""
Дан список слов. Сгенерировать новый список с перевернутыми словами
"""


def main():
    one_listt = ['Антон', 'Дима', 'Гений', 'Котик']
    two_listt = [i[::-1] for i in one_listt]
    print(two_listt)


if __name__ == '__main__':
    main()
