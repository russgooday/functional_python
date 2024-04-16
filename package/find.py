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

# Some Examples
if __name__ == "__main__":

    # create a predicate function
    find_greater_than_2 = find(lambda x: x > 2)
    find_all_greater_than_2 = find_all(lambda x: x > 2)

    # find using a predicate function
    print(find_greater_than_2([1, 2, 3, 4, 5])) # 3
    print(find_all_greater_than_2([1, 2, 3, 4, 5])) # [3, 4, 5]

    students = [
        {'name': 'John', 'age': 25},
        {'name': 'Jane', 'age': 22},
        {'name': 'John', 'age': 30}
    ]

    # using a dictionary to find a match
    print(find({'name': 'John', 'age': 25}, students)) # {'name': 'John', 'age': 25}

    # using a dictionary to find all matches
    print(find_all({'name': 'John'}, students))
    # [{'name': 'John', 'age': 25}, {'name': 'John', 'age': 30}]

    # using a list [key, value]
    print(find(['b', 2], [{'a': 3, 'b': 2}, {'a': 2, 'b': 9}])) # {'a': 3, 'b': 2}

    # using regex to match strings
    import re
    print(find_all(re.compile(r'[a-z][2-4]'), ['a1', 'b2', 'c3', 'd4', 'e5'])) # ['b2', 'c3', 'd4']
