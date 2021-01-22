from funcs.funcs_11 import quadratic_equation


def test_one_1():
    result_1, result_2 = quadratic_equation(10, 2, 2)
    assert result_1 == result_2 == 0


def test_one_2():
    result_1, result_2 = quadratic_equation(1, 2, 1)
    assert result_1 == result_2 == -1


def test_one_3():
    result_1, result_2 = quadratic_equation(2, 1, -1)
    assert result_1 == 0.5
    assert result_2 == -1


def test_two_1():
    result_1, result_2 = quadratic_equation(1, 0, -1)
    assert result_1 == -1
    assert result_2 == 1


def test_two_2():
    result_1, result_2 = quadratic_equation(1, 0, 2)
    assert result_1 == result_2 == 0


def test_three():
    result_1, result_2 = quadratic_equation(4, 2, 0)
    assert result_1 == 0
    assert result_2 == -0.5
