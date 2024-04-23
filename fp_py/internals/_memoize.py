''' Decorator that memoizes the result of a function call. '''

# Basic implementation of a memoize
# A decorator that caches the result of a function call
def _memoize(fn):
    cache = {}

    def inner_fn(*args):
        # convert any lists to tuples so they can be hashed
        key = tuple(tuple(x) if isinstance(x, list) else x for x in args)

        if key in cache:
            return cache[key]

        cache[key] = fn(*args)
        return cache[key]

    return inner_fn

# An example of using the memoize decorator
if __name__ == "__main__":
    # create a memoized version of the fibonacci function
    @_memoize
    def fib(n):
        if n <= 1:
            return n

        return fib(n-2) + fib(n-1)

    for x in range(0, 40):
        print(f'{x}: {fib(x)}')

    print(fib.__closure__[0].cell_contents)  # prints the cache dictionary
