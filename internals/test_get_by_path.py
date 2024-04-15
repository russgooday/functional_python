import pytest
from path import _get_by_path, get_by_path

# Test cases for _get_by_path
test_case_get_by_path = [
    # Test case 1
    (['a', 'b', 'c'], {'a': {'b': {'c': 1}}}, 1),
    # Test case 2
    (['a', 'b'], {'a': {'b': {'c': 1}}}, {'c': 1}),
    # Test case 3
    (['a', 'b', 'c'], {'a': 1}, None),
    # Test case 4
    (['a', 'b', 'c'], {'a': {'b': 2}}, None),
    # Mix of lists and dicts
    (['a', 1, 'c'], {'a': [{}, {'c': 1}]}, 1),
    # Various key types
    ([True, 1.5, 0, 'x'], {True: {1.5: {0: {'x': 2}}}}, 2)
]

@pytest.mark.parametrize("input_list, obj, expected_output", test_case_get_by_path)
def test_get_by_path(input_list, obj, expected_output):
    assert get_by_path(input_list, obj) == expected_output

def test_get_by_path_with_default():
    assert _get_by_path(['a', 'b', 'c'], {'a': {'b': {'c': 1}}}, 2) == 1
    assert _get_by_path(['a', 'b', 'c'], {'a': {'b': {}}}, 2) == 2
