"""
Дана целочисленная матрица А[n,m].
Посчитать количество элементов матрицы,
превосходящих среднее арифметическое значение элементов матрицы
и сумма индексов которых четна.[02-4.2-BL23]
"""
from random import randint


def create_matrix(n, m):
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(randint(1, 9))
        matrix.append(row)
    return matrix


def min_matrix(matrix):
    m = matrix[0][0]
    for row in matrix:
        for elem in row:
            if elem < m:
                m = elem
    return m


def max_matrix(matrix):
    m = matrix[0][0]
    for row in matrix:
        for elem in row:
            if elem > m:
                m = elem
    return m


def my_average(a, b):
    average = (a + b) / 2
    return average


def my_summ(matrix):
    tmp = []
    for v in range(len(matrix)):
        for z in range(len(matrix)):
            if (v + z) % 2 == 0:
                tmp += [matrix[v][z]]
    return tmp


def result(summ, avarage):
    count = 0
    for elem in summ:
        if elem > avarage:
            count += 1
    return count


def main():
    n = int(input("Введите количество раз: "))
    m = int(input("Введите количество раз: "))
    print_matrix = create_matrix(n, m)
    summ = my_summ(print_matrix)
    max_number = max_matrix(print_matrix)
    min_number = min_matrix(print_matrix)
    average_number = my_average(min_number, max_number)
    print_result = result(summ, average_number)
    print(f'Вот матрица: {print_matrix}')
    print(f'Вот среднее арифметическое значение: {average_number}')
    print(f'Вот элемменты, где сумма индексов четна: {summ}')
    print(f'Вот количество элементов матрицы, '
          f'превосходящих среднее арифметическое '
          f'значение элементов матрицы и '
          f'сумма индексов которых четна - {print_result} ')


if __name__ == '__main__':
    main()
