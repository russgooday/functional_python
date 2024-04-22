''' creates curried versions of given functions '''
from package.internals._parameters import Parameters

__ = {'placeholder': True}

def is_placeholder(*args: any) -> bool:
    '''Returns a tuple of booleans indicating if the arguments are placeholders'''
    return tuple(isinstance(arg, dict) and arg.get('placeholder', False) for arg in args)

def _curry_2(fn: callable)->callable:
    '''returns a curried version of a function with an arity of 2'''
    if not callable(fn):
        raise TypeError('fn must be a callable')

    def get_fn(case, placeholder, x=None, y=None):
        return {
            1: {(False,): lambda _y: fn(x, _y)},

            2: {(True, False): lambda _x: fn(_x, y),
                (False, True): lambda _y: fn(x, _y)}

        }[case][placeholder]

    def curried_fn(*args):

        if len(args) == 0:
            return curried_fn

        placeholders = is_placeholder(*args)
        # all args are values so return the result
        if placeholders.count(False) == 2:
            return fn(*args)
        # all placeholders so return the curried function
        if placeholders.count(True) == 2:
            return curried_fn
        return get_fn(len(args), placeholders, *args)

    return curried_fn


def _curry_3(fn: callable)->callable:
    '''returns a curried version of a function with an arity of 3'''
    if not callable(fn):
        raise TypeError('fn must be a callable')

    def get_fn(case, placeholder, x=None, y=None, z=None):
        return {
            1: {(False,): lambda _y, _z: fn(x, _y, _z)},

            2: {(True, False): lambda _x, _z: fn(_x, y, _z),
                (False, True): lambda _y, _z: fn(x, _y, _z),
                (False, False): lambda _z: fn(x, y, _z)},

            3: {(True, True, False): lambda _x, _y: fn(_x, _y, z),
                (True, False, True): lambda _x, _z: fn(_x, y, _z),
                (False, True, True): lambda _y, _z: fn(x, _y, _z),
                (True, False, False): lambda _x: fn(_x, y, z),
                (False, True, False): lambda _y: fn(x, _y, z),
                (False, False, True): lambda _z: fn(x, y, _z)}

        }[case][placeholder]

    def curried_fn(*args):
        num_args = len(args)

        if num_args == 0:
            return curried_fn

        placeholders = is_placeholder(*args)

        if placeholders.count(False) == 3:
            return fn(*args)
        if placeholders.count(True) == 3:
            return curried_fn
        if placeholders.count(True) == num_args - 1:
            return _curry_2(get_fn(num_args, placeholders, *args))
        return get_fn(num_args, placeholders, *args)

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
    num_params = Parameters(fn).non_defaults

    def partial(*args1):
        if num_params - len(args1) > 0:
            return lambda *args2: partial(*[*args1, *args2])

        return fn(*args1)

    return partial

if __name__ == "__main__":
    def add(a, b, c):
        return a + b + c

    curry_add = _partial_curry(add)
    print('curry_add a,b,c:', curry_add(1)(2)(3))       # add a,b,c: 6
    print('curry_add a,b,c:', curry_add(1, 2)(3))       # add a,b,c: 6
    print('curry_add a,b,c:', curry_add(1)(2, 3))       # add a,b,c: 6
    print('curry_add a,b,c:', curry_add(1, 2, 3))       # add a,b,c: 6

    def add_2(a, b):
        return a + b

    curry_add = _curry_2(add_2)
    print('curry2_add a,b:',curry_add(1)(2))           # add a,b: 3
    print('curry2_add a,b:',curry_add(__, 2)(4))       # add a,b: 6
    print('curry2_add a,b:',curry_add(3, __)(4))       # add a,b: 7
    print('curry2_add a,b:',curry_add(__, __)(4, 2))   # add a,b: 6

    def add_3(a, b, c):
        return a + b + c

    curry3_add = _curry_3(add_3)
    print('curry3_add a,b,c:', curry3_add(1)(2)(3))             # curry3_add: 6
    print('curry3_add a,b,c:', curry3_add(__, 2, 3)(1))         # curry3_add: 6
    print('curry3_add a,b,c:', curry3_add(__, __, 3)(1, 2))     # curry3_add: 6
    print('curry3_add a,b,c:', curry3_add(__, 2, __)(1, 3))     # curry3_add: 6

    print(Parameters(str.split).parameters)
    print(Parameters(str.split).paramcount)

    split = _curry_2(str.split)
    split_on_comma = split(__, ',')
    join = _curry_2(str.join)
    join_on_dash = join('-')

    lst = split_on_comma('a,b,c,d')
    print(lst)  # ['a', 'b', 'c', 'd']
    string = join_on_dash(lst)
    print(string)  # a-b-c-d
