''' creates curried versions of given functions '''
from fp_py.internals._parameters import Parameters
from fp_py.internals import __
# pylint: disable=E1120

def get_placeholder_pos(*args: any) -> tuple[bool]:
    '''Returns a tuple of booleans indicating which arguments are placeholders'''
    return tuple(isinstance(arg, dict) and arg.get('placeholder', False) for arg in args)

def _curry_2(fn: callable)->callable:
    '''returns a curried version of a function with an arity of 2'''
    if not callable(fn):
        raise TypeError('fn must be a callable')

    fn_arity = 2
    x = y = None

    placeholder_fns = {
        1: {(False,): lambda _y: fn(x, _y)},

        2: {(True, False): lambda _x: fn(_x, y),
            (False, True): lambda _y: fn(x, _y)}
    }

    def curried_fn(*args):
        nonlocal x, y

        num_args = len(args)

        if not args:
            return curried_fn
        if num_args == 1:
            x = args[0]
        elif num_args == 2:
            x, y = args

        placeholder_pos = get_placeholder_pos(*args)

        if placeholder_pos.count(False) == fn_arity:
            return fn(*args)

        if placeholder_pos.count(True) == fn_arity:
            return curried_fn

        return placeholder_fns[num_args][placeholder_pos]

    return curried_fn


def _curry_3(fn: callable)->callable:
    '''returns a curried version of a function with an arity of 3'''

    if not callable(fn):
        raise TypeError('fn must be a callable')

    fn_arity = 3
    x = y = z = None

    placeholder_fns = {
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
    }

    def curried_fn(*args):
        nonlocal x, y, z
        num_args = len(args)

        if not args:
            return curried_fn
        if num_args == 1:
            x = args[0]
        elif num_args == 2:
            x, y = args
        elif num_args == 3:
            x, y, z = args

        placeholder_pos = get_placeholder_pos(*args)
        # all args are values so invoke the function and return a result
        if placeholder_pos.count(False) == fn_arity:
            return fn(*args)
        # all args are placeholders so return the curried function
        if placeholder_pos.count(True) == fn_arity:
            return curried_fn
        # only one value is bound so return a partially applied function
        # for the next two arguments
        if placeholder_pos.count(True) == num_args - 1:
            return _curry_2(placeholder_fns[num_args][placeholder_pos])

        return placeholder_fns[num_args][placeholder_pos]

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

    if num_params == 0:
        return fn

    def partial(*args1):
        if num_params - len(args1) > 0:
            return lambda *args2: partial(*[*args1, *args2])

        return fn(*args1)

    return partial

if __name__ == "__main__":
    @_curry_2
    def add_2(a, b):
        return a + b

    print('curry2_add a,b:',add_2(1)(2))           # add a,b: 3
    print('curry2_add a,b:',add_2(__, 2)(4))       # add a,b: 6
    print('curry2_add a,b:',add_2(3, __)(4))       # add a,b: 7
    print('curry2_add a,b:',add_2(__, __)(4, 2))   # add a,b: 6

    @_curry_3
    def add_3(a, b, c):
        return a + b + c

    print('curry3_add a,b,c:', add_3(1)(2)(3))             # curry3_add: 6
    print('curry3_add a,b,c:', add_3(__, 2, 3)(1))         # curry3_add: 6
    print('curry3_add a,b,c:', add_3(__, __, 3)(1, 2))     # curry3_add: 6
    print('curry3_add a,b,c:', add_3(__, 2, __)(1, 3))     # curry3_add: 6

    @_partial_curry
    def add_with_default(a, b, c=2):
        return a + b + c

    print('add_with_default:', add_with_default(1)(2))  # 5

    # Example with built-ins
    split = _curry_2(str.split)
    split_on_comma = split(__, ',')

    join = _curry_2(str.join)
    join_on_dash = join('-')

    letters = split_on_comma('a,b,c,d')
    print(letters)  # ['a','b','c','d']
    str_letters = join_on_dash(letters)
    print(str_letters)  # a-b-c-d
