from funcs import funcs_08


def test_arithmetic():
    assert funcs_08.arithmetic(2, 4, 6, 9, 10, 11, 7, 12) == 7.625


def test_geometric():
    assert funcs_08.geometric(2, 4, 6, 9, 10, 11, 7, 12) == 6.685662740671728
