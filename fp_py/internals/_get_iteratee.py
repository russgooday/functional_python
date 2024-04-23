'''
    get_iteratee creates predicate or mapping functions
'''

import re
from fp_py.internals._parameters import _adjust_params_count

def _get_iteratee(value):
    '''
        Takes a function, or an object, or a string or regex to match with
        and returns a predicate or mapping function
    '''
    if callable(value):
        # function: returns a wrapped function that calls the given function
        # with the correct number of arguments
        return _adjust_params_count(value)

    if isinstance(value, list):
        k, v = value
        # [ 'key', value ]: returns True if key and value are found in object
        return lambda obj: obj.get(k) == v

    if isinstance(value, dict):
        # { 'key1': value1, ... }: returns True if properties correspond in both objects
        return lambda obj: all(k in obj and obj[k] == v for k, v in value.items())

    if isinstance(value, str):
        # 'key': returns value of object['key'] or None
        return lambda obj: obj.get(value, None)

    if isinstance(value, re.Pattern):
        # regex: returns true if a string match is found
        return value.search

    raise ValueError("Unsupported value type")
