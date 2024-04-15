''' flat and flat_map functions '''

from package.internals._get_iteratee import _get_iteratee

def _flat(lst: list, depth=float('Inf'))-> list:
    '''
        flattens a nested list recursively to a given depth
        e.g. _flat([1, [2, 3, [4, 5]]], 2) -> [1, 2, 3, 4, 5]
        if depth is ommited, flattens completely
    '''
    if depth < 1:
        return lst

    flattend = []

    for v in lst:
        flattend += _flat(v, depth-1) if isinstance(v, list) else [v]

    return flattend


def _flat_map(fn: callable, lst: list)-> list:
    '''
        takes a predicate function and a list, and maps
        the elements returning a flattend list
    '''

    mapping = _get_iteratee(fn)
    flattend = []

    if callable(fn):
        list_copy = [*lst]
        for i, v in enumerate(lst):
            flattend += mv if isinstance((mv:= mapping(v, i, list_copy)), list) else [mv]
    else:
        for v in lst:
            flattend += mv if isinstance((mv:= mapping(v)), list) else [mv]

    return flattend
