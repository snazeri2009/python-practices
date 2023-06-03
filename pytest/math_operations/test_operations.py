import math_operations.operations as operations


def test_add():
    assert operations.add(2, 3) == 5
    assert operations.add(-1, 1) == 0
    assert operations.add(0, 0) == 0

def test_subtract():
    assert operations.subtract(5, 2) == 3
    assert operations.subtract(2, 5) == -3
    assert operations.subtract(0, 0) == 0

def test_multiply():
    assert operations.multiply(2, 3) == 6
    assert operations.multiply(-2, 3) == -6
    assert operations.multiply(0, 5) == 0

def test_divide():
    assert operations.divide(6, 3) == 2
    assert operations.divide(10, -2) == -5
    assert operations.divide(0, 5) == 0

    try:
        operations.divide(5, 0)
        assert False  # The ZeroDivisionError should be raised
    except ZeroDivisionError:
        assert True
