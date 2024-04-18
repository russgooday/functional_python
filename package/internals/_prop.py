''' property functions '''


def _pad_list_end(lst: list, targ_len:int, fill=None):
    """
        Pad the list to the target length with a fill value.

        e.g.
            _pad_list_end([1, 2], 3) → [1, 2, None, None]
            _pad_list_end([1, 2, 3], 2) → [1, 2, 3]

        @returns: a shallow clone
    """
    padding = max(0, targ_len + 1 - len(lst))
    return  [*lst, *[fill] * padding]


def _get_prop(key:str|int, obj:dict|list, default=None):
    '''
        tries to get property from dict or lists

        @param obj: the object to search e.g. dict, list
        @param key: the key to search for
        @param default: the value to return if key is not found

        @return: value or default
    '''
    try:
        return obj[key]
    except (KeyError, IndexError, TypeError):
        return default


def _set_prop(key:str|int, val:any, obj:dict|list):
    '''
        sets property

        @param key: the key to set
        @param value: the value to set
        @param obj: the object to be modified

        @return: modfied clone of object
    '''
    if isinstance(key, int) and isinstance(obj, list):
        lst = _pad_list_end(obj, key)
        lst[key] = val
        return lst

    obj = dict(enumerate(obj) if isinstance(obj, list) else obj.items())
    obj[key] = val
    return obj


def _prop_equals(val, key:str|int, obj:dict|list):
    '''
        compares property to given value

        @param value: the value to set
        @param key: the key to set
        @param obj: the object to be modified

        @return: bool
    '''
    return _get_prop(key, obj, False) == val
