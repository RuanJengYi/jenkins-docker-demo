import pytest

def add(a, b):
    return a+b

def test_add_pass():
    assert add(1, 1) == 2

# def test_add_fail():
#     assert add(1, 1) == 4
