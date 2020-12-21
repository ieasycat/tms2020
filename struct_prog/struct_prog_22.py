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


def max_matrix(matrix):
    for i in range(len(matrix)):
        tmp = matrix[i]
        m = 0
        for elem in tmp:
            if elem > m:
                m = elem
        matrix[i][i] = m
        print(f'New numbers - {m}')
    return matrix


def main():
    print("Введите значения для квадратной матрицы.")
    one_number = int(input("Введите 1-ое число: "))
    two_number = int(input("Введите 2-ое число: "))
    x = create_matrix(one_number, two_number)
    print(f'Old matrix - {x}')
    new_matrix = max_matrix(x)
    print(f'New matrix - {new_matrix}')


if __name__ == '__main__':
    main()
