''' flatten functions '''
from package.internals._curry import _curry_2
from package.internals._flat import _flat, _flat_map

# flat
# listA → int → listB
# params: (lst, depth)
# returns: list
# Description: flatten a list to a given depth or completely flatten it
flat = _flat

# flat_map
# callable → listA → listB
# params: (fn, lst)
# returns: list
# Description: takes a predicate function and a list, and
# maps the elements returning a concatenated list
flat_map = _curry_2(_flat_map)

# Running the tests
if __name__ == "__main__":
    def double(x):
        return [x, x]

    def identity(x):
        return x

    double_curried = flat_map(double)

    print(flat([1, [2, 3, [4, 5]]], 2)) # [1, 2, 3, 4, 5]
    print(flat_map(double, [1, 2, 3])) # [1, 1, 2, 2, 3, 3]
    print(flat_map(identity, [1, 2, 3])) # [1, 2, 3]
    print(flat_map(identity, [[1], [2], [3]])) # [1, 2, 3]
    print(double_curried([1, 2, 3])) # [1, 1, 2, 2, 3, 3]
    print([*map(double_curried, [[1],[2],[3]])]) # [[1, 1], [2, 2], [3, 3]]
