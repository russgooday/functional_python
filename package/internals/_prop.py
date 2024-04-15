''' property functions '''
def _get_prop(key:str|int, obj:dict|list, default=None):
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

def _prop_equals(val, key:str|int, obj:dict|list):
    return _get_prop(key, obj, False) == val
