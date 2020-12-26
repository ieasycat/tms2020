"""
Дан массив целых чисел A.
Найти суммы положительных и отрицательных элементов массива,
используя функцию определения суммы. [02-5.1-BL21]
"""


def summ(numbers):
    positive_summ = 0
    negative_summ = 0
    for number in numbers:
        if number > 0:
            positive_summ += number
        elif number < 0:
            negative_summ += number
    return positive_summ, negative_summ


def main():
    listt = [2, -3, 7, -9, 3, 9, -15, 10]
    pos, neg = summ(listt)
    print(f'Сумма положительных чисел равна: {pos}')
    print(f'Сумма отрицательных чисел равна: {neg}')


if __name__ == '__main__':
    main()
