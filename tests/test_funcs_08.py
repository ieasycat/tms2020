from funcs.funcs_08 import arithmetic, geometric


def test_arithmetic():
    assert arithmetic(2, 4, 6, 9, 10, 11, 7, 12) == 7.625


def test_geometric():
    assert geometric(2, 4, 6, 9, 10, 11, 7, 12) == 6.685662740671728
