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


def count_element(matrix):
    count = 0
    for row in matrix:
        for elem in row:
            count += 1
    return count


def my_average(matrix, count):
    summ = 0
    for row in matrix:
        for elem in row:
            summ += elem
    avarage = summ / count
    return avarage


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
    print_element = count_element(print_matrix)
    average_number = my_average(print_matrix, print_element)
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
