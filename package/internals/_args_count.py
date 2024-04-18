'''This module contains functions to work with the number of arguments'''

def _args_count(fn: callable, dictionary=False)->int:
    '''
        Returns number of parameters in given function

        if dictionary flag is True, returns a dictionary of parameter properties.
    '''
    if not callable(fn):
        raise TypeError('fn must be a callable')

    if not dictionary:
        return fn.__code__.co_argcount

    params = fn.__code__.co_argcount
    defaults = len(fn.__defaults__ or ())

    return {
        'params': params,
        'defaults': defaults,
        'non_defaults': params - defaults
    }


def _adjust_args_count(fn: callable) -> callable:
    '''
    Creates a wrapper function that calls the given function with
    the correct number of arguments. Insufficent arguments will still raise an error.

    :param fn: the callback function

    :return: a function that calls the callback
     with the correct number of arguments
    '''
    if not callable(fn):
        raise TypeError('fn must be a callable')

    # wraps the function to ignore extra arguments
    return lambda *args: fn(*args[:_args_count(fn)])
