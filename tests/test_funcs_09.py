from funcs import funcs_09


def test_score():
    result = funcs_09.score((1, 2, 3, 2, 4))
    assert {1: 1, 2: 2, 3: 1, 4: 1} == result
