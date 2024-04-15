''' Path functions get_by_path, set_by_path and path_equals '''
from package.internals._prop import _get_prop

def _pad_list(lst: list, target_length: int, fill_value=None):
    """Pad the list to the target length with the specified fill value."""
    if len(lst) >= target_length:
        return lst[:]
    # pad the list with the fill value to the target length
    return lst[:] + [fill_value] * (target_length - len(lst))

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

    # if key is an integer make a shallow copy
    # lists will be padded up to the given key index number
    # e.g. with a key of 2 ['a', 'b'] → ['a', 'b', None]
    if isinstance(key, int) and isinstance(obj, list):
        obj = _pad_list(obj, key + 1)

    # if key is string make a shallow copy of source object
    # lists will be converted to dictionaries with indexes becoming keys
    # e.g. ['a', 'b'] → ['0': 'a', '1': 'b']
    if isinstance(key, str):
        obj = dict(enumerate(obj) if isinstance(obj, list) else obj.items())

    if rest_of_keys:
        target = _get_prop(obj, key)

        if not isinstance(target, (list, dict)):
            target = [] if isinstance(rest_of_keys[0], int) else {}

        obj[key] = _set_by_path(rest_of_keys, value, target)
    else:
        obj[key] = value

    return obj

def _path_equals(val: any, keys: list, obj: dict|list) -> bool:
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

# Running the tests
if __name__ == "__main__":
    print(_set_by_path(['a', 'b', 'c'], 42, {'a': 5})) # {'a': {'b': {'c': 42}}}
    print(_get_by_path(['pet', 'age'], {'pet': {'age': 10}})) # 10
    print(_path_equals(10, ['pet', 'age'], {'pet': {'age': 10}})) # True
