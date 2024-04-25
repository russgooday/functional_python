''' Path functions get_by_path, set_by_path and path_equals '''
from fp_py.internals._prop import _get_prop, _set_prop
from fp_py.internals._get_iteratee import _get_iteratee

def _get_by_path(path: list, obj: list|dict, default=None) -> any:
    '''
    gets a nested property value following a given path

    e.g.    getByPath(['pet', 'age'], user)
            equivalent to `user and user['pet'] and user['pet']['age']`

    :param path: a list of keynames(str) or/and indexes(int) that make the path
    :param obj: the object to search e.g. dict, list

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
        e.g. setByPath(['a', 'b', 'c'], 42, {'a': 5}) → {'a': {'b': {'c': 42}}}

        :param path: a list of keynames(str) or/and indexes(int) that make the path
        :param value: the value to set
        :param obj: the object to search e.g. dict, list

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

            pathEquals(['pet', 'age'], 3, user) # true
            pathEquals(['pet', 'name'], 'Spot', user) # true

    :param keys: a list of keynames(str) or/and indexes(int) that make the path
    :param val: the value to compare
    :param obj: the object to search e.g. dict, list

    :return: bool
    '''
    return _get_by_path(keys, obj) == val


def _path_satisfies(fn: callable, keys: list, obj: dict|list) -> bool:
    '''
    checks if a nested property value following a given path satisfies a given predicate

    e.g.    user = {'pet': {name: 'Fido', 'age': 10}}

            path_satisfies(['pet', 'age'], lambda x: x > 3, user) # true
            path_satisfies({'name': 'Fido', 'age': 10}, ['pet'], user) # true
            path_satisfies(['name', 'Spot'], ['pet'], user) # false

    :param fn: a predicate function or iteratee
    :param keys: a list of keynames(str) or/and indexes(int) that make the path
    :param obj: the object to search e.g. dict, list

    :return: bool
    '''
    predicate = _get_iteratee(fn)
    return predicate(_get_by_path(keys, obj))
