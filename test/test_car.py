"""
Создать файл test_car в пакете test.
Протестировать конструктор, метод увеличения скорости, уменьшения скорости,
остановки и разворота класса Car в файле oop/car10
"""

import unittest
from oop.car10 import Car


class CarTestCase(unittest.TestCase):
    def test_speed_increase(self):
        my_car = Car('Opel', 'Tigra', 1996)
        my_car.speed_increase()
        self.assertEqual(my_car.speed, 5)

    def test_speed_reduction(self):
        my_car = Car('Opel', 'Tigra', 1996, 5)
        my_car.speed_reduction()
        self.assertEqual(my_car.speed, 0)

    def test_speed_reset(self):
        my_car = Car('Opel', 'Tigra', 1996, 15)
        my_car.speed_reset()
        self.assertEqual(my_car.speed, 0)

    def test_speed_reversal(self):
        my_car = Car('Opel', 'Tigra', 1996, 5)
        my_car.speed_reversal()
        self.assertEqual(my_car.speed, -5)
