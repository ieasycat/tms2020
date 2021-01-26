from funcs.funcs_16 import palindrome


def test_palindrome():
    assert palindrome(('лол', 'привет', 'река'))
    assert not palindrome(('привет', 'река'))
