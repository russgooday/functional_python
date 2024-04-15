'''Test cases for _reduce and _reduce_right functions'''
from reduce import _reduce, _reduce_right

def test_reduce():
    # Test case with addition
    assert _reduce(lambda x, y: x + y, 0, [1, 2, 3, 4]) == 10

    # Test case with multiplication
    assert _reduce(lambda x, y: x * y, 1, [1, 2, 3, 4]) == 24

    # Test case with strings concatenation
    assert _reduce(lambda x, y: x + y, '', ['a', 'b', 'c', 'd', 'e']) == 'abcde'

    # Test case with subtraction
    assert _reduce(lambda x, y: x - y, 10, [1, 2, 3, 4]) == 0

def test_reduce_right():
    # Test case with addition
    assert _reduce_right(lambda x, y: x + y, 0, [1, 2, 3, 4]) == 10

    # Test case with multiplication
    assert _reduce_right(lambda x, y: x * y, 1, [1, 2, 3, 4]) == 24

    # Test case with strings concatenation
    assert _reduce_right(lambda x, y: x + y, '', ['a', 'b', 'c', 'd', 'e']) == 'edcba'

    # Test case with subtraction
    assert _reduce_right(lambda x, y: x - y, 10, [1, 2, 3, 4]) == 0
