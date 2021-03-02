"""
Создать файл test_matrix в пакете test.
Протестировать конструктор,магический метод __str__ класса Matrix.
В отдельном классе теста протестировать функции по работе с матрицами.
"""

import unittest
from oop.matrix import Matrix, \
    max_elem_for_matrix, min_elem_for_matrix, summ_elem_for_matrix


class MatrixTestCase(unittest.TestCase):
    def setUp(self):
        self.matrix = Matrix(3, 2, 0, 0)

    def test_matrix(self):
        data = self.matrix
        self.assertEqual(data.data, [[0, 0], [0, 0], [0, 0]])
        self.assertEqual(data.n, 3)
        self.assertEqual(data.m, 2)
        self.assertEqual(data.a, 0)
        self.assertEqual(data.b, 0)

    def test_str(self):
        data = self.matrix
        pr = data.__str__()
        self.assertEqual(pr, '[0, 0]\n[0, 0]\n[0, 0]')


class MethodsTestCase(unittest.TestCase):
    def setUp(self):
        self.matrix = Matrix(3, 2, 1, 1)

    def test_max_elem(self):
        max_elem = max_elem_for_matrix(self.matrix)
        self.assertEqual(max_elem, 1)

    def test_min_elem(self):
        min_elem = min_elem_for_matrix(self.matrix)
        self.assertEqual(min_elem, 1)

    def test_sum_elem(self):
        summ = summ_elem_for_matrix(self.matrix)
        self.assertEqual(summ, 6)
