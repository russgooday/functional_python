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

if __name__ == "__main__":
    add = _curry_2(lambda x, y: x + y)
    add_5 = add(5)
    print(add_5(10)) # 15
