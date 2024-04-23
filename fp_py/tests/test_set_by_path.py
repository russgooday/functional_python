''' Tests for the set_by_path function. '''
import pytest

from fp_py.path import set_by_path

# Tests for set_by_path function
test_cases = [
    ([0], 'a', ['b', 'c'], ['a', 'c']),
    (['a', 'b', 'c'], 42, {'a': 5}, {'a': {'b': {'c': 42}}}),
    (['a', 0], 'b', {'a': ['c']}, {'a': ['b']}),
    (['a', 1], 'd', {'a': ['b', 'c']}, {'a': ['b', 'd']}),
    (['a', 2], 'e', {'a': ['b', 'c']}, {'a': ['b', 'c', 'e']}),
    (['a', 2], 'e', {'a': []}, {'a': [None, None, 'e']}),
    ([1], 42, {'a': 5}, {1: 42, 'a': 5}),
    (['a'], 42, ['a', 'b', 'c'], {0: 'a', 1: 'b', 2: 'c', 'a': 42})
]

@pytest.mark.parametrize("path, value, src, expected", test_cases)
def testset_by_path(path, value, src, expected):
    assert set_by_path(path, value, src) == expected

def test_original_dict_is_not_modified():
    src = {'a': {'b': {'c': 42}}}
    copy = set_by_path(['a', 'b', 'c'], 44, src)
    assert src['a']['b']['c'] != copy['a']['b']['c']

def test_original_list_is_not_modified():
    src = {'a': ['b', 'c']}
    copy = set_by_path(['a', 1], 'd', src)
    assert src['a'][1] != copy['a'][1]

def test_empty_path_returns_value():
    assert set_by_path([], 42, {'a': 5}) == 42

def test_non_primitives_copies():
    src = {'a': [1, 2, 3]}
    copy = set_by_path(['a', 1], 42, src)
    src['a'].append(4)
    assert len(copy['a']) != len(src['a'])

def test_curried_function():
    user1 = { 'name': 'Bob', 'address': { 'postCode': 'N4 5BL'} }
    # user2 = { 'name': 'Sue', 'address': { 'postCode': 'NW1 6RQ'} }
    user3 = { 'name': 'Rita' }
    # users = [ user1, user2, user3 ]

    set_postcode = set_by_path(['address', 'postCode'])
    set_postcode_nw5_6st = set_postcode('NW5 6ST')

    assert set_postcode('NW1 6RQ', user1) == {'name': 'Bob', 'address': {'postCode': 'NW1 6RQ'}}
    assert set_postcode('NW1 6RQ', user3) == {'name': 'Rita', 'address': {'postCode': 'NW1 6RQ'}}
    assert set_postcode_nw5_6st(user3) == {'name': 'Rita', 'address': {'postCode': 'NW5 6ST'}}

    # all_users = [set_postcode_nw5_6st(user) for user in users]
    # assert all(user['address']['postCode'] == 'NW5 6ST' for user in all_users)
