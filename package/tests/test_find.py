import re
import pytest
from package.internals._find import _find, _find_all

# Sample data
users = [
    {'name': 'John', 'age': 25, 'active': True},
    {'name': 'Jane', 'age': 30, 'active': False},
    {'name': 'Jim', 'age': 35, 'active': True},
    {'name': 'Jack', 'age': 40, 'active': False},
    {'name': 'Jill', 'age': 45, 'active': True},
    {'name': 'Joe', 'age': 30, 'active': False}
]

strings = ['hello', 'world', 'foo', 'bar', 'baz']


# Tests for _find function
def test_find_by_dict():
    assert _find({'name': 'Jane'}, users) == {'name': 'Jane', 'age': 30, 'active': False}

def test_find_by_lambda():
    assert _find(lambda user: user['age'] == 25, users) == {'name': 'John', 'age': 25, 'active': True}

def test_find_by_list():
    assert _find(['age', 35], users) == {'name': 'Jim', 'age': 35, 'active': True}

def test_find_all_by_dict():
    assert _find_all({'age': 30, 'active': False}, users) == [
        {'name': 'Jane', 'age': 30, 'active': False},
        {'name': 'Joe', 'age': 30, 'active': False}
    ]

def test_find_all_by_regex():
    assert _find_all(re.compile(r'^b'), strings) == ['bar', 'baz']

# Running the tests
if __name__ == "__main__":
    pytest.main()
