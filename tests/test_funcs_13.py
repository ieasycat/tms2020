from funcs.funcs_13 import summ


def test_summ():
    result_1, result_2 = summ([2, -3, 7, -9, 3, 9, -15, 10])
    assert result_1 == 31
    assert result_2 == -27


def test_summ_two():
    result_1, result_2 = summ([2, -3, 7, -14, 3, 9, -15, 12])
    assert result_1 == 33
    assert result_2 == -32
