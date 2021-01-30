"""
Создать файл matrix.py.
Создать класс Matrix.
Атрибуты - data(содержит саму матрицу - список списков), n, m.
Определить конструктор(с параметрами(передача размерности:
n, m и диапазона случайных чисел: a, b),
по-умолчанию(матрица 5 на 5 где все элементы равны нулю), копирования),
переопределить магический метод __str__ для красивого вывода.
Описать функции, которые принимают на вход объект класса Matrix.
Функции позволяют искать максимальный элемент матрицы, минимальный,
сумму всех элементов.
Создать в файле main.py матрицу.
Воспользоваться всеми описанными функциями и методами
"""
from random import randint


class Matrix:
    def __init__(self, data, n=5, m=5, a=0, b=0):
        self.data = [[randint(a, b) for i in range(m)]for row in range(n)]
        self.n = n
        self.m = m
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.data}'

    @property
    def max_elem_for_matrix(self):
        max_elem = self.data[0][0]
        for row in self.data:
            for elem in row:
                if elem > max_elem:
                    max_elem = elem
        return max_elem

    @property
    def min_elem_for_matrix(self):
        min_elem = self.data[0][0]
        for row in self.data:
            for elem in row:
                if elem < min_elem:
                    min_elem = elem
        return min_elem

    @property
    def summ_elem_for_matrix(self):
        summ = 0
        for row in self.data:
            for elem in row:
                summ += elem
        return summ


def main():
    my_matrix = Matrix([], 3, 3, 1, 9)
    print(my_matrix)
    print(my_matrix.max_elem_for_matrix)
    print(my_matrix.min_elem_for_matrix)
    print(my_matrix.summ_elem_for_matrix)


if __name__ == '__main__':
    main()
