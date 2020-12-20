"""
В массиве целых чисел с количеством элементов 19
определить максимальное число и заменить
им все четные по значению элементы. [02-4.1-BL19]
"""

from random import randint


def create(matrix):
    matrix_one = []
    for i in range(matrix):
        matrix_one.append(randint(1, 20))
    return matrix_one


def max_matrix(matrix):
    m = matrix[0]
    for elem in matrix:
        if elem > m:
            m = elem
    return m


def replacement(matrix, x):
    for i in matrix:
        if i % 2 == 0:
            b = matrix.index(i)
            matrix[b] = x
    return matrix


def main():
    matrix = create(19)
    max_number = max_matrix(matrix)
    new_matrix = replacement(matrix, max_number)
    print(f"Это максимальное число в масиве - {max_number}")
    print(f"А это сам масив - {new_matrix}")


if __name__ == '__main__':
    main()
