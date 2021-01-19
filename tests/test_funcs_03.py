"""
Тестируем функцию 'funcs/funcs_03'
"""

from funcs import funcs_03


def test_factorial():
    result = funcs_03.my_factorial(4)
    assert result == 24


def test_factorial_ver_2():
    result = funcs_03.my_factorial(6)
    assert result == 720
