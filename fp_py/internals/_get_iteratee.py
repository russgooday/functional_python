'''
    get_iteratee creates predicate or mapping functions
'''

import re
from fp_py.internals._parameters import _adjust_params_count
from fp_py.internals._prop import _get_prop, _prop_equals

def _all_props_match(props, target_obj):
    '''
        Returns True if all properties correspond in both objects
    '''
    if isinstance(props, dict) and isinstance(target_obj, dict):
        return all(_prop_equals(v, k, target_obj) for k, v in props.items())

    return False


def _get_iteratee(value):
    '''
        Takes a function, or an object, or a string or regex to match with
        and returns a predicate or mapping function
    '''
    if not value:
        # None: returns identity function
        return lambda x: x

    if callable(value):
        # function: returns a wrapped function that calls the given function
        # with the correct number of arguments
        return _adjust_params_count(value)

    if isinstance(value, (list, tuple)) and len(value) == 2:
        # [ 'key', value ]: returns True if key and value are found in object
        return lambda obj: _prop_equals(value[1], value[0], obj)

    if isinstance(value, dict):
        # { 'key1': value1, ... }: returns True if properties correspond in both objects
        return lambda obj: _all_props_match(value, obj)

    if isinstance(value, str):
        # 'key': returns value of object['key'] or None
        return lambda obj: _get_prop(value, obj)

    if isinstance(value, re.Pattern):
        # regex: returns true if a string match is found
        return value.search

    raise ValueError("Unsupported value type")
