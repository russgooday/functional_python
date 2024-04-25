'''Path module for getting and setting values in nested dictionaries.'''

from fp_py.internals._curry import _curry_2, _curry_3
from fp_py.internals._path import (
    _get_by_path,
    _set_by_path,
    _path_equals,
    _path_satisfies
)

__all__ = ['get_by_path', 'set_by_path', 'path_equals']

def _get_by_path_or_none(path, obj):
    return _get_by_path(path, obj, None)

# Curried functions

# get_by_path
# list → obj → any|None
# params: (path, obj)
# returns: any|None
# Description: gets a nested property value following a given path
get_by_path = _curry_2(_get_by_path_or_none)

# set_by_path
# list → any → obj → obj
# params: (path, value, obj)
# returns: obj
# Description: Set the value of a nested property at the specified path.
set_by_path = _curry_3(_set_by_path)

# path_equals
# any → list → obj → bool
# params: (value, path, obj)
# returns: bool
# Description: Check if the nested property value is equal to the provided value.
path_equals = _curry_3(_path_equals)


# path_satisfies
# (any → bool) → list → obj → bool
# params: (fn|iteratee, path, obj)
# returns: bool
# Description: Check if the nested property value satisfies the provided predicate.
path_satisfies = _curry_3(_path_satisfies)


# Examples
if __name__ == "__main__":
    print(set_by_path(['a', 'b', 'c'], 42, {'a': 5}))               # {'a': {'b': {'c': 42}}}
    print(set_by_path(['a', 1], 'd', {'a': ['b', 'c']}))            # {'a': ['b', 'd']}
    print(get_by_path(['pet', 'age'], {'pet': {'age': 10}}))        # 10
    print(path_equals(10, ['pet', 'age'], {'pet': {'age': 10}}))                    # True
    print(path_satisfies(lambda x: x > 5, ['pet', 'age'], {'pet': {'age': 10}}))    # True
    print(path_satisfies(['c', 3], ['a', 'b'], {'a': {'b': {'c': 3}}}))             # True
