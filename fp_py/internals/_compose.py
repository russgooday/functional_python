from fp_py.internals._reduce import _reduce, _reduce_right

def _compose_two(f, g):
    '''compose 2 functions right to left order'''
    return lambda *args: f(g(*args))

def _compose_three(f, g, h):
    '''compose 2 functions right to left order'''
    return lambda *args: f(g(h(*args)))

def _compose(*fns):
    '''
        compose multiple functions right to left order
        last argument can be a function of any arity, followed by unary functions
    '''
    return lambda *args: _reduce_right(lambda f, g: g(f), fns[-1](*args), fns[:-1])

def _pipe(fn, *fns):
    '''
        compose multiple functions left to right order
        first argument can be a function of any arity, followed by unary functions
    '''
    return lambda *args: _reduce(lambda f, g: g(f), fn(*args), fns)
