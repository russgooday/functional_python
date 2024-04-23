'''Test cases for reduce and reduce_right functions'''
from fp_py.reduce import reduce, reduce_right

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def subtract(x, y):
    return x - y

def test_reduce():
    # Test case with addition
    assert reduce(add, 0, [1, 2, 3, 4]) == 10

    # Test case with multiplication
    assert reduce(multiply, 1, [1, 2, 3, 4]) == 24

    # Test case with strings concatenation
    assert reduce(add, '', ['a', 'b', 'c', 'd', 'e']) == 'abcde'

    # Test case with subtraction
    assert reduce(subtract, 10, [1, 2, 3, 4]) == 0

    # Test case with curried function
    concat_string = reduce(add, '')
    assert concat_string(['a', 'b', 'c', 'd', 'e']) == 'abcde'

    # Test case with empty list
    assert reduce(add, 0, []) == 0

def test_reduce_right():
    # Test case with addition
    assert reduce_right(add, 0, [1, 2, 3, 4]) == 10

    # Test case with multiplication
    assert reduce_right(multiply, 1, [1, 2, 3, 4]) == 24

    # Test case with strings concatenation
    assert reduce_right(add, '', ['a', 'b', 'c', 'd', 'e']) == 'edcba'

    # Test case with subtraction
    assert reduce_right(subtract, 10, [1, 2, 3, 4]) == 0

    # Test case with curried function
    concat_string = reduce_right(add, '')
    assert concat_string(['a', 'b', 'c', 'd', 'e']) == 'edcba'

    # Test case with empty list
    assert reduce_right(add, 0, []) == 0
