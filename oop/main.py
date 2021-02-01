"""
Создать в файле main.py матрицу.
Воспользоваться всеми описанными функциями и методами.
"""

from oop.matrix import Matrix, max_elem_for_matrix, \
    min_elem_for_matrix, summ_elem_for_matrix


def main():
    my_matrix = Matrix(3, 3, 1, 9)
    my_matrix.__str__()
    print(max_elem_for_matrix(my_matrix.data))
    print(min_elem_for_matrix(my_matrix.data))
    print(summ_elem_for_matrix(my_matrix.data))


if __name__ == '__main__':
    main()
