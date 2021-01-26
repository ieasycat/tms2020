from funcs.funcs_17 import sin1, factorial
import math


def test_sin1():
    assert sin1(math.pi/6, 0.01) == 0.5000021325887924
    assert sin1(math.pi/6, 0.0001) == 0.4999999918690232


def test_factorial():
    # По факту это факториал из 21
    assert factorial(10) == 51090942171709440000
    # По факту это факториал из 7
    assert factorial(3) == 5040
