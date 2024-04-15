''' property functions '''
from curry import _curry_2, _curry_3

def _get_prop(obj:dict|list, key:str|int, default=None):
    '''
        tries to get property from dict or lists

        :param obj: the object to search e.g. dict, list
        :param key: the key to search for
        :param default: the value to return if key is not found

        :return: value or default
    '''
    try:
        return obj[key]
    except (KeyError, IndexError, TypeError):
        return default


def _get_prop_or_none(obj:dict|list, key:str|int):
    return _get_prop(obj, key)


def _prop_equals(val, key, obj):
    return _get_prop(obj, key) == val

# curried functions
prop_equals = _curry_3(_prop_equals)

get_prop = _curry_2(_get_prop_or_none)
