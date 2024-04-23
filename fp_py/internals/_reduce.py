'''This module contains the implementation of the reduce and reduce_right functions.'''

from fp_py.internals._parameters import _adjust_params_count

def _reduce(fn:callable, accumulator:any, lst:list)-> any:
    it = enumerate(lst)
    reducer = _adjust_params_count(fn)

    if accumulator is None:
        _, accumulator = next(it)

    for i, value in it:
        accumulator = reducer(accumulator, value, i)

    return accumulator

def _reduce_right(fn:callable, accumulator:any, lst:list)-> any:
    return _reduce(fn, accumulator, reversed(lst))

if __name__ == '__main__':
    def add(x, y):
        return x + y

    def multiply(x, y):
        return x * y

    print(_reduce(add, 0, [1, 2, 3, 4, 5])) # 15
    print(_reduce(multiply, 1, [1, 2, 3, 4, 5])) # 120
    print(_reduce_right(add, None, ['a','b','c','d','e'])) # edcba
