'''This module contains the implementation of the reduce and reduce_right functions.'''

from package.internals._args_count import _adjust_args_count

def _reduce(fn:callable, accumulator:any, lst:list)-> any:
    it = enumerate(lst)
    reducer = _adjust_args_count(fn)

    if accumulator is None:
        _, accumulator = next(it)

    for i, value in it:
        accumulator = reducer(accumulator, value, i)

    return accumulator

def _reduce_right(fn:callable, accumulator:any, lst:list)-> any:
    return _reduce(fn, accumulator, reversed(lst))
