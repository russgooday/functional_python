def _get_prop(key:str|int, obj:dict|list, default=None):

    try:
        return obj[key]
    except (KeyError, IndexError, TypeError):
        return default


def _pad_list_end(lst: list, targ_len:int, fill=None):
    """
    Pad the list to the target length with fill value.
    @returns: a shallow clone
    """
    padding = targ_len + 1 - len(lst)
    return  [*lst] if padding < 1 else [*lst, *[fill] * (padding)]

def _set_prop(key:str|int, val:any, obj:dict|list):
    if isinstance(key, int) and isinstance(obj, list):
        lst = _pad_list_end(obj, key)
        lst[key] = val
        return lst

    obj = dict(enumerate(obj) if isinstance(obj, list) else obj.items())
    obj[key] = val
    return obj


def _set_by_path(path: list, value: any, obj: dict|list) -> dict|list:
    if not path:
        return value

    key, *rest_of_keys = path

    if rest_of_keys:
        next_obj = _get_prop(key, obj)

        if not isinstance(next_obj, (list, dict)):
            next_obj = [] if isinstance(rest_of_keys[0], int) else {}

        value = _set_by_path(rest_of_keys, value, next_obj)

    return _set_prop(key, value, obj)

if __name__ == '__main__':
    print(_set_by_path(['a', 'b', 'c'], 42, {'a': 5}))      # {'a': {'b': {'c': 42}}}
    print(_set_by_path(['a', 1], 'd', {'a': ['b', 'c']}))   # {'a': ['b', 'd']}
    print(_set_by_path([0, 1, 2], 'd', []))                 # [[None, [None, None, 'd']]]
