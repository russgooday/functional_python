from fp_py.internals._where import _where, _where_equals
from fp_py.internals._curry import _curry_2

where = _curry_2(_where)
where_equals = _curry_2(_where_equals)

# Examples
if __name__ == '__main__':
    # single quotes on object keys
    props = {'a': 10, 'b': 20, 'c': 30}

    print(where_equals(props, {'a': 10, 'b': 20, 'c': 30, 'd': 40})) # True
    print(where_equals(props, {'a': 10, 'b': 20, 'c': 40})) # False
