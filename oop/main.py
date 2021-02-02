"""
Создать в файле main.py матрицу.
Воспользоваться всеми описанными функциями и методами.
"""

from oop.matrix import Matrix, max_elem_for_matrix, \
    min_elem_for_matrix, summ_elem_for_matrix


def main():
    my_matrix = Matrix(3, 3, 1, 9)
    print(my_matrix)
    print(max_elem_for_matrix(my_matrix))
    print(min_elem_for_matrix(my_matrix))
    print(summ_elem_for_matrix(my_matrix))


if __name__ == '__main__':
    main()
