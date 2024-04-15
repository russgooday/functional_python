''' find items in a list'''
from package.internals._curry import _curry_2
from package.internals._find import _find, _find_all

# find
# callable → list → any|None
# params: (fn, lst)
# returns: any|None
# Description: takes a predicate function/iteratee and a list, and
# returns the first found item to match the predicate, or None
# e.g. find(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]) -> 2
find = _curry_2(_find)

# find_all
# callable → list → list
# params: (fn, lst)
# returns: list
# Description: takes a predicate function/iteratee and a list, and
# returns all items that match the predicate or an empty list
# e.g. find_all(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]) -> [2, 4]
find_all = _curry_2(_find_all)

# Running the tests
if __name__ == "__main__":
    def is_even(x):
        return x % 2 == 0

    print(find(is_even, [1, 2, 3, 4, 5])) # 2
    print(find_all(is_even, [1, 2, 3, 4, 5])) # [2, 4]
    print(find_all(is_even, [1, 3, 5])) # []
    print(find_all(is_even, [])) # []
