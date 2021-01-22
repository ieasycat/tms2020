from funcs.funcs_12 import is_power_n, my_count


def test_is_power_n():
    result_1 = is_power_n(16, 2)
    result_2 = is_power_n(16, 3)
    assert result_1
    assert not result_2


def test_my_count():
    result_1 = my_count(64)
    result_2 = my_count(120)
    assert result_1 == 3
    assert result_2 == 0
