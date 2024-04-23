import re
import pytest
from fp_py.find import find, find_all

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


# Tests for find function
def test_find_by_dict():
    assert find({'name': 'Jane'}, users) == {'name': 'Jane', 'age': 30, 'active': False}

def test_find_by_lambda():
    assert find(lambda user: user['age'] == 25, users) == {'name': 'John', 'age': 25, 'active': True}

def test_find_curried():
    find_jane = find({'name': 'Jane'})
    assert find_jane(users) == {'name': 'Jane', 'age': 30, 'active': False}

def test_find_by_list():
    assert find(['age', 35], users) == {'name': 'Jim', 'age': 35, 'active': True}

def test_find_all_by_dict():
    assert find_all({'age': 30, 'active': False}, users) == [
        {'name': 'Jane', 'age': 30, 'active': False},
        {'name': 'Joe', 'age': 30, 'active': False}
    ]

def test_find_all_by_regex():
    assert find_all(re.compile(r'^b'), strings) == ['bar', 'baz']

def test_find_all_curried():
    find_all_active = find_all({'active': True})
    assert find_all_active(users) == [
        {'name': 'John', 'age': 25, 'active': True},
        {'name': 'Jim', 'age': 35, 'active': True},
        {'name': 'Jill', 'age': 45, 'active': True}
    ]

# Running the tests
if __name__ == "__main__":
    pytest.main()
