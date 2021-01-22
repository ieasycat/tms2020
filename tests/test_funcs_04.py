from funcs import funcs_04


def test_create():
    matrix = funcs_04.create(3)
    assert len(matrix) == 3
    for i in range(3):
        assert len(matrix[i]) == 3
        for j in range(3):
            assert matrix[i][j] > 1
            assert matrix[i][j] < 10
