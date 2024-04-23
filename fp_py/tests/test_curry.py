import pytest
from fp_py.curry import curry

# add
def add(a, b, c):
    return a + b + c

# add with default parameter
def add_with_default(a, b, c=2):
    return a + b + c

def test_partial_curry_3_arguments():
    curry_add = curry(add)
    assert curry_add(1)(2)(3) == 6
    assert curry_add(1, 2)(3) == 6
    assert curry_add(1)(2, 3) == 6
    assert curry_add(1, 2, 3) == 6

def test_partial_curry_3_with_default_arguments():
    curry_add = curry(add_with_default)
    assert curry_add(1)(2) == 5
    with pytest.raises(TypeError) as excinfo:
        curry_add(1)(2)(3)
    assert "'int' object is not callable" in str(excinfo.value)
