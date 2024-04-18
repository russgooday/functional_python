''' Partial currying function. '''
from package.internals._curry import _partial_curry

# curry
# a.k.a. partial curry
# Binds arguments to a function and returns a new curried function.
# Unlike a strict curry function, multiple arguments can be passed at once.
# With the correct number of arguments given, the function will be invoked.
#
#
# e.g.
#   def add(a, b, c):
#       return a + b + c
#
#   curry_add = curry(add)
#   curry_add(1)(2)(3) == 6
#   curry_add(1, 2)(3) == 6
#   curry_add(1)(2, 3) == 6
#   curry_add(1, 2, 3) == 6
#
# With default parameter
#   def add_with_default(a, b, c=2):
#       return a + b + c
#
#   curry_add_with_default = curry(add_with_default)
#   curry_add_with_default(1)(2) == 5
#   curry_add_with_default(1)(2, 3) == 6
#   curry_add_with_default(1)(2)(3) raises TypeError with "'int' object is not callable"
#
# @param fn: function
# @return: curried function|Any
curry = _partial_curry
