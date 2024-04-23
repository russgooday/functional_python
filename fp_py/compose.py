''' composition functions '''
from fp_py.internals._compose import _compose, _pipe, _compose_two, _compose_three

# compose_two
# params: (f, g)
# returns: composed callable
# Description: compose 2 functions right to left order
compose_two = _compose_two

# compose_three
# params: (f, g, h)
# returns: composed callable
# Description: compose 3 functions right to left order
compose_three = _compose_three

# compose
# params: (fns)
# returns: composed callable
# Description: compose multiple functions right to left order
# last argument can be a function of any arity, followed by unary functions
compose = _compose

# pipe
# params: (fn, fns)
# returns: composed callable
# Description: compose multiple functions left to right order
# first argument can be a function of any arity, followed by unary functions
pipe = _pipe
