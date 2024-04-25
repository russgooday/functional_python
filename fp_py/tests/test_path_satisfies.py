import pytest
from fp_py.path import path_satisfies

# Test cases for _path_satisfies
test_case_path_satisfies = [
    # Test case 1
    (lambda x: x % 2 == 0, ['a', 'b', 'c'], {'a': {'b': {'c': 2}}}, True),
    # Test case 2
    ({'c': 1, 'd': 2}, ['a', 'b'], {'a': {'b': {'c': 1, 'd': 2, 'e': 3}}}, True),
    # Test case 3
    ({'c': 1, 'd': 2}, ['a', 'b'], {'a'}, False),
    # Test case 4
    (['a', 2], ['a', 'b', 'c'], {'a': 1}, False),
    # Test case 5
    (['c', 3], ['a', 'b'], {'a': {'b': {'c': 3}}}, True),
    # Mix of lists and dicts
    (lambda s: s.upper() == 'SHOUT!', ['a', 1, 'c'], {'a': [{}, {'c': 'shout!'}]}, True),
    # Various key types
    (['x', 2], [True, 1.5, 0], {True: {1.5: {0: {'x': 2}}}}, True)
]


@pytest.mark.parametrize("predicate, path, obj, expected_output", test_case_path_satisfies)
def test_path_satisfies(predicate, path, obj, expected_output):
    assert path_satisfies(predicate, path, obj) == expected_output

if __name__ == '__main__':
    pytest.main()
