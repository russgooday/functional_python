''' find.py '''
from fp_py.internals._get_iteratee import _get_iteratee

def _find(fn: callable, lst: list):
    '''
        takes a predicate function and a list, and returns
        the first found item to match the predicate, or None
    '''
    predicate = _get_iteratee(fn)

    if callable(fn):
        return next(
            (v for i,v in enumerate(lst) if predicate(v, i)), None
        )

    return next((v for v in lst if predicate(v)), None)


def _find_last(fn: callable, lst: list):
    '''
        takes a predicate function and a list, and returns
        the last found item to match the predicate, or None
    '''
    predicate = _get_iteratee(fn)

    if callable(fn):
        i = len(lst)
        return next(
            (v for v in reversed(lst) if predicate(v, (i:=i-1))), None
        )

    return next((v for v in reversed(lst) if predicate(v)), None)


def _find_all(fn: callable, lst: list) -> list:
    '''
        takes a predicate function and a list, and returns
        all items that match the predicate or an empty list
    '''
    predicate = _get_iteratee(fn)

    if callable(fn):
        return [v for i, v in enumerate(lst) if predicate(v, i)]

    return [v for v in lst if predicate(v)]
