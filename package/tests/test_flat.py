''' Tests for the _flat and _flat_map functions '''
import pytest
from package.flat import flat, flat_map

# flat test data
list_3_deep = [1, [2, [3, [4, 5]], 6], 7, [8, 9, 10]]
list_flat = [1, 2, 3, 4, 5, 6]
list_empty = []
list_varied_types = [1, 'a', [2, 'b'], {'c': 3}, (4, 'd')]

# flat_map test data
list_nums = [1, 2, 3, 4, 5, 6]
list_of_dicts = [{'x': 1}, {'x': 2}, {'y': 3}]


# Tests for _find function
def test_flatten_by_one():
    assert flat(list_3_deep, 1) == [1, 2, [3, [4, 5]], 6, 7, 8, 9, 10]

def test_flatten_by_two():
    assert flat(list_3_deep, 2) == [1, 2, 3, [4, 5], 6, 7, 8, 9, 10]

def test_flatten_completely():
    assert flat(list_3_deep) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_flatten_empty_list():
    assert flat(list_empty) == []

def test_flatten_varied_types():
    assert flat(list_varied_types) == [1, 'a', 2, 'b', {'c': 3}, (4, 'd')]

def test_flatten_map_duplicate():
    def duplicate(x):
        return [x, x]
    assert flat_map(duplicate, list_nums) == [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]

def test_flatten_map_with_list_properties():
    # returns booleans for each dict that matches {x: 2}
    assert flat_map(['x', 2], list_of_dicts) == [False, True, False]

def test_flatten_map_with_str_property():
    # returns values for each dict that has 'x' property
    assert flat_map('x', list_of_dicts) == [1, 2, None]

def test_flatten_map_with_filtering_lambda():
    def is_even(x):
        return x if x % 2 == 0 else []
    assert flat_map(is_even, list_nums) == [2, 4, 6]

# Running the tests
if __name__ == "__main__":
    pytest.main()
