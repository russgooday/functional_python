'''
    get_iteratee creates predicate or mapping functions
'''
import re

from fp_py.internals._parameters import _adjust_params_count
from fp_py.prop import get_prop, prop_equals
from fp_py.where import where_equals


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
        return prop_equals(value[1], value[0])

    if isinstance(value, dict):
        # { 'key1': value1, ... }: returns True if properties correspond in both objects
        return where_equals(value)

    if isinstance(value, str):
        # 'key': returns value of object['key'] or None
        return get_prop(value)

    if isinstance(value, re.Pattern):
        # regex: returns true if a string match is found
        return value.search

    raise ValueError("Unsupported value type")
