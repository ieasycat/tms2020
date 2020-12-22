"""
Дана целочисленная квадратная матрица. Найти в каждой строке наи-
больший элемент и поменять его местами с элементом главной диагонали.
[02-4.2-ML22]
"""
from random import randint


def create_matrix(n, m):
    list_one = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(randint(1, 9))
        list_one.append(row)
    return list_one


def new_matrix(matrix):
    for i, numbers in enumerate(matrix):
        m = 0
        for elem in numbers:
            if elem > m:
                m = elem
        matrix[i][i] = m
        print(f'New numbers - {m}')
    return matrix


def main():
    print("Введите значения для квадратной матрицы.")
    one_number = int(input("Введите 1-ое число: "))
    two_number = int(input("Введите 2-ое число: "))
    print_matrix = create_matrix(one_number, two_number)
    print(f'Old matrix - {print_matrix}')
    print_new = new_matrix(print_matrix)
    print(f'New matrix - {print_new}')


if __name__ == '__main__':
    main()
