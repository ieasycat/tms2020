"""
Реализовать функцию возвращающую матрицу.
На вход принимает n - размерность матрицы,
random_from(по-умолчанию 1), random_to(по-умолчанию(9)).
"""
from random import randint


def create(n, r_from=1, r_to=9):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(randint(r_from, r_to))
        matrix.append(row)
    return matrix


def main():
    numbers = int(input("Введите первое число: "))
    print_matrix = create(numbers)
    print(f'Вот Ваша матрица: {print_matrix}')


if __name__ == '__main__':
    main()
