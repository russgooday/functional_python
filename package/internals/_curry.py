''' creates curried versions of given functions '''
from package.internals._args_count import _args_count

def _curry_2(fn: callable)->callable:
    '''returns a curried version of a function with an arity of 2'''

    if not callable(fn):
        raise TypeError('fn must be a callable')

    if _args_count(fn) != 2:
        raise ValueError('Callable function must have 2 parameters')

    def curried_fn(*args):
        if len(args) == 2:
            return fn(args[0], args[1])
        if len(args) == 1:
            return lambda x: fn(args[0], x)
        if len(args) == 0:
            return curried_fn

        raise ValueError('Callable function takes too many arguments')

    return curried_fn


def _curry_3(fn: callable)->callable:
    '''returns a curried version of a function with an arity of 3'''

    if not callable(fn):
        raise TypeError('fn must be a callable')

    if _args_count(fn) != 3:
        raise ValueError('Callable function must have 3 parameters')

    def curried_fn(*args):
        num_args = len(args)

        if num_args == 3:
            return fn(*args)
        if num_args == 2:
            return lambda x: fn(args[0], args[1], x)
        if num_args == 1:
            return _curry_2(lambda x, y: fn(args[0], x, y))
        if num_args == 0:
            return curried_fn

        raise ValueError('Callable function takes too many arguments')

    return curried_fn

# Partial Curry
def _partial_curry(fn):
    '''
        Binds arguments to a function and returns a new function.
        With the correct number of arguments the function will be called.

        @param fn: function
        @return: function|Any

        e.g.
        def add(a, b, c, d=4):
            return a + b + c + d

        fn_1 = add_partial(1)       # (a=1, b=?, c=?, d=4) → fn
        fn_1_2 = fn_1(2)            # (a=1, b=2, c=?, d=4) → fn
        fn_1_2(3)                   # (a=1, b=2, c=3, d=4) → fn → 10
        fn_1_2(3, 9)                # (a=1, b=2, c=3, d=9) → fn → 15

        fn_2 = add_partial(2, 5)    # (a=2, b=5, c=?, d=4) → fn
        fn_2(4)                     # (a=2, b=5, c=4, d=4) → fn → 15
    '''
    params = _args_count(fn, dictionary=True)['non_defaults']

    def partial(*args1):
        if params - len(args1) > 0:
            return lambda *args2: partial(*[*args1, *args2])

        return fn(*args1)

    return partial

if __name__ == "__main__":
    def add(a, b, c):
        return a + b + c

    partial_add = _partial_curry(add)
    print('add a,b,c:', partial_add(1)(2)(3)) # add a,b,c: 6
    print('add a,b,c:', partial_add(1, 2)(3)) # add a,b,c: 6
    print('add a,b,c:', partial_add(1)(2, 3)) # add a,b,c: 6
    print('add a,b,c:', partial_add(1, 2, 3)) # add a,b,c: 6
