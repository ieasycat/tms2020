"""
Написать программу для работы с матрицами:
1. Создание
2. Вывод
3. Сумма всех элементов
4. Нахождение максимального элемента
5. Нахождение минимального элемента.
"""
from random import randint


def create(n):
    matrix_one = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(randint(1, 9))
        matrix_one.append(row)
    return matrix_one


def print_matrix(matrix):
    for row in matrix:
        for elem in row:
            print(elem, end=" ")
        print()


def summ_matrix(matrix):
    summ = 0
    for row in matrix:
        for elem in row:
            summ += elem
    return summ


def max_matrix(matrix):
    m = matrix[0][0]
    for row in matrix:
        for elem in row:
            if elem > m:
                m = elem
    return m


def min_matrix(matrix):
    m = matrix[0][0]
    for row in matrix:
        for elem in row:
            if elem < m:
                m = elem
    return m


def main():
    print_create = create(3)
    print_matrix(print_create)
    print_summ = summ_matrix(print_create)
    print_max = max_matrix(print_create)
    print_min = min_matrix(print_create)
    print(f'{print_summ} {print_max} {print_min}')


if __name__ == '__main__':
    main()
