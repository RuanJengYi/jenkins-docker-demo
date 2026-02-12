import pytest

def add(a, b):
    return a+b

def test_add_pass():
    assert add(1, 1) == 2
def test_add_pass_2():
    assert add(1, 3) == 4
    
# def test_add_fail():
#     assert add(1, 1) == 4


