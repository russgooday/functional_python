''' Path functions get_by_path, set_by_path and path_equals '''
from fp_py.internals._prop import _get_prop, _set_prop
from fp_py.internals._get_iteratee import _get_iteratee

def _get_by_path(path: list, obj: list|dict, default=None) -> any:
    '''
    gets a nested property value following a given path

    e.g.    _get_by_path(['pet', 'age'], user)
            equivalent to `'pet' in user and user['pet'].get('age', default)`

    _get_by_path(path, obj, default(optional))

    :param path: a list of keynames(str) or/and indexes(int) that make the path
    :param obj: the object to search e.g. dict, list
    :param default: optional value to return if key is not found — default is None

    :return: value or default
    '''
    value = obj

    for key in path:
        try:
            value = value[key]
        except (KeyError, IndexError, TypeError):
            return default

    return value


def _set_by_path(path: list, value: any, obj: dict|list) -> dict|list:
    '''
        Set the value in the dictionary at the specified path.
        e.g. _set_by_path(['a', 'b', 'c'], 42, {'a': 5}) → {'a': {'b': {'c': 42}}}

        _set_by_path(path, value, obj) -> dict|list

        :param path: a list of keynames(str) or/and indexes(int) that make the path
        :param value: the value to set
        :param obj: the object to search e.g. dict, list

        Does not mutate the original object, but returns a new object with the updated value
        :return: dict|list
    '''
    if not path:
        return value

    key, *rest_of_keys = path

    if rest_of_keys:
        next_obj = _get_prop(key, obj)

        if not isinstance(next_obj, (list, dict)):
            next_obj = [] if isinstance(rest_of_keys[0], int) else {}

        value = _set_by_path(rest_of_keys, value, next_obj)

    return _set_prop(key, value, obj)


def _path_equals(val: any, keys: list, obj: dict|list) -> bool:
    '''
    checks if a nested property value following a given path is equal to a given value

    e.g.    user = {'pet': {name: 'Fido', 'age': 10}}

            _path_equals(10, ['pet', 'age'], user)      # True
            _path_equals('Spot', ['pet', 'name'], user) # False

    _path_equals(val, path, obj) -> bool

    :param val: the value to compare
    :param keys: a list of keynames(str) or/and indexes(int) that make the path
    :param obj: the object to search e.g. dict, list

    :return: bool
    '''
    return _get_by_path(keys, obj) == val


def _path_satisfies(fn: callable, keys: list, obj: dict|list) -> bool:
    '''
    checks if a nested property value following a given path satisfies a given predicate

    e.g.    user = {'pet': {name: 'Fido', 'age': 10}}

            # predicate function
            _path_satisfies(lambda x: x > 3, ['pet', 'age'], user)          # True

            # iteratee matches object properties
            _path_satisfies({'name': 'Fido', 'age': 10}, ['pet'] , user)    # True

            # iteratee matches tuple key and value pair
            _path_satisfies(('name', 'Spot'), ['pet'], user)                # False

    _path_satisfies(predicate, path, obj) -> bool

    :param predicate: a predicate function or iteratee
    :param keys: a list of keynames(str) or/and indexes(int) that make the path
    :param obj: the object to search e.g. dict, list

    :return: bool
    '''
    predicate = _get_iteratee(fn)
    return predicate(_get_by_path(keys, obj))

if __name__ == '__main__':
    user = {'name': 'Jane', 'pet': {'name': 'Fido', 'age': 10}}

    # _get_by_path examples
    print(_get_by_path(['pet', 'age'], user))    # 10
    print(_get_by_path(['pet', 'name'], user))   # 'Fido'

    # _set_by_path examples
    print(_set_by_path(['pet', 'name'], 'Spot', user))  # {'name': 'Jane', 'pet': {'name': 'Spot', 'age': 10}}
    print(_set_by_path(['b', 1], 42, {'a': 5}))         # {'a': 5, 'b': [None, 42]}
    print(_set_by_path(['a', 'b', 'c'], 42, {'a': 5}))  # {'a': {'b': {'c': 42}}}

    # _path_equals examples
    print(_path_equals(10, ['pet', 'age'], user))       # True
    print(_path_equals('Spot', ['pet', 'name'], user))  # False


    # _path_satifies examples

    # predicate function
    print(_path_satisfies(lambda x: x > 3, ['pet', 'age'], user))       # True
    # iteratee matches object properties
    print(_path_satisfies({'name': 'Fido', 'age': 10}, ['pet'] , user)) # True
    # iteratee matches tuple key and value pair
    print(_path_satisfies(('name', 'Spot'), ['pet'], user))             # False
