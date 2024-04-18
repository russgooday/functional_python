''' Decorator that memoizes the result of a function call. '''
from package.internals._timing import _timing
from package.internals._memoize import _memoize

# Basic implementation of a memoize
# A decorator that caches the result of a function call
memoize = _memoize

# An example of using the memoize decorator
if __name__ == "__main__":
    def fib(n):
        if n <= 1:
            return n

        return fib(n-2) + fib(n-1)

    @memoize
    def fib_memoized(n):
        if n <= 1:
            return n

        return fib_memoized(n-2) + fib_memoized(n-1)

    @_timing
    def test_fib():
        for x in range(0, 40):
            fib(x)

    @_timing
    def test_fib_memoized():
        for x in range(0, 40):
            fib_memoized(x)

    test_fib()          # func:'test_fib' args:[(), {}] took: 26.1276 sec
    test_fib_memoized() # func:'test_fib_memoized' args:[(), {}] took: 0.0000 sec
