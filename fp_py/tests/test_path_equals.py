import pytest
from fp_py.path import path_equals

# Test cases for _path_equals
test_case_path_equals = [
    # Test case 1
    (1, ['a', 'b', 'c'], {'a': {'b': {'c': 1}}}, True),
    # Test case 2
    (1, ['a', 'b'], {'a': {'b': {'c': 1}}}, False),
    # Test case 3
    (1, ['a', 'b', 'c'], {'a': 1}, False),
    # Test case 4
    (2, ['a', 'b'], {'a': {'b': 2}}, True),
    # Mix of lists and dicts
    (1, ['a', 1, 'c'], {'a': [{}, {'c': 1}]}, True),
    # Various key types
    (2, [True, 1.5, 0, 'x'], {True: {1.5: {0: {'x': 2}}}}, True)
]


@pytest.mark.parametrize("val, path, obj, expected_output", test_case_path_equals)
def test_path_equals(val, path, obj, expected_output):
    assert path_equals(val, path, obj) == expected_output
