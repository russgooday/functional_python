''' list reduce functions '''
from fp_py.internals._curry import _curry_3
from fp_py.internals._reduce import _reduce, _reduce_right

__all__ = ['reduce', 'reduce_right']

# reduce
# callable → any → list → any
# params: (fn, accumulator, lst)
# returns: any
# Description: reduces a list to a single value using a given function
# e.g. reduce(lambda acc, char: acc + char, 0, ['a', 'b', 'c']) -> 'abc'
reduce = _curry_3(_reduce)

# reduce_right
# callable → any → list → any
# params: (fn, accumulator, lst)
# returns: any
# Description: reduces a list to a single value using a given function in reverse order
# e.g. reduce_right(lambda acc, char: acc + char, 0, ['a', 'b', 'c']) -> 'cba'
reduce_right = _curry_3(_reduce_right)

# Running the tests
if __name__ == "__main__":
    def add(acc, num):
        return acc + num

    def product(acc, num):
        return acc * num

    # Test cases with strings concatenation
    print(reduce(add, '', ['a', 'b', 'c', 'd', 'e'])) # 'abcde'
    print(reduce_right(add, '', ['a', 'b', 'c', 'd', 'e'])) # 'edcba'

    # Test cases with curried function
    get_product = reduce(product, 1)
    print(get_product([1, 2, 3, 4])) # 24
