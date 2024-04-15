''' Path functions get_by_path, set_by_path and path_equals '''
from curry import _curry_2, _curry_3
from prop import _get_prop

def _pad_list(lst: list, target_length: int, fill_value=None):
    """Pad the list to the target length with the specified fill value."""
    if len(lst) >= target_length:
        return lst[:]
    # pad the list with the fill value to the target length
    return lst[:] + [fill_value] * (target_length - len(lst))

def _get_by_path(path, obj, default=None):
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


def _get_by_path_or_none(path, obj):
    return _get_by_path(path, obj)


def _set_by_path(path: list, value: any, src: dict|list):
    '''
        Set the value in the dictionary at the specified path.
        e.g. setByPath(['a', 'b', 'c'], 42, {'a': 5}) → {'a': {'b': {'c': 42}}}

        :param path: a list of keynames(str) or/and indexes(int) that make the path
        :param value: the value to set
        :param src: the object to search e.g. dict, list

        :return: dict|list
    '''
    if not path:
        return value

    key, *rest_of_keys = path

    # if key is an integer make a shallow copy
    # lists will be padded up to the given key index number
    # e.g. with a key of 2 ['a', 'b'] → ['a', 'b', None]
    if isinstance(key, int) and isinstance(src, list):
        src = _pad_list(src, key + 1)

    # if key is string make a shallow copy of source object
    # lists will be converted to dictionaries with indexes becoming keys
    # e.g. ['a', 'b'] → ['0': 'a', '1': 'b']
    if isinstance(key, str):
        src = dict(enumerate(src) if isinstance(src, list) else src.items())

    if rest_of_keys:
        target = _get_prop(src, key)

        if not isinstance(target, (list, dict)):
            target = [] if isinstance(rest_of_keys[0], int) else {}

        src[key] = _set_by_path(rest_of_keys, value, target)
    else:
        src[key] = value

    return src

def _path_equals(val, keys, obj):
    '''
    checks if a nested property value following a given path is equal to a given value

    e.g.    pathEquals(['pet', 'age'], 3, user)
            equivalent to `user and user['pet'] and user['pet']['age'] == 3`

    :param keys: a list of keynames(str) or/and indexes(int) that make the path
    :param val: the value to compare
    :param obj: the object to search e.g. dict, list

    :return: bool
    '''
    return _get_by_path(keys, obj) == val

# Curried functions
get_by_path = _curry_2(_get_by_path_or_none)

set_by_path = _curry_3(_set_by_path)

path_equals = _curry_3(_path_equals)
