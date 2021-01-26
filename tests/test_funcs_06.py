from funcs import funcs_06


def test_summ_max():
    summ, max = funcs_06.sum_and_max(3, 4, 8, 10, 3, 5)
    assert summ == 33
    assert max == 10


def test_negative_summ_max():
    summ, max = funcs_06.sum_and_max(-3, -4, -8, -10, -3, -5)
    assert summ == -33
    assert max == -3
