from funcs.funcs_10 import calc


def test_calc():
    assert calc(5) == 3.618033988749895


def test_calc_2():
    assert calc(19) == 11.679449471770337


def test_calc_3():
    assert calc(12) == 7.732050807568877
