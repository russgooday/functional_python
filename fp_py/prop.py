''' Module for working with properties of objects. '''

from fp_py.internals._curry import _curry_2, _curry_3
from fp_py.internals._prop import _get_prop, _set_prop, _prop_equals

def _get_prop_or_none(key:str|int, obj:dict|list) -> any:
    return _get_prop(key, obj)

# curried functions

# get_prop
# str|int → obj → any|None
# params: (key, obj)
# returns: any|None
# Description: Get the value of a property in an object.
get_prop = _curry_2(_get_prop_or_none)

# set_prop
# str|int → any -> obj → obj
# params: (key, val, obj)
# returns: obj
# Description: Returns clone of obj with property set.
set_prop = _curry_3(_set_prop)

# prop_equals
# any → str|int → obj → bool
# params: (val, key, obj)
# returns: bool
# Description: Check if a property value is equal to the provided value.
prop_equals = _curry_3(_prop_equals)

# Running the tests
if __name__ == "__main__":
    print(get_prop('age', {'age': 21}))         # 21
    print(get_prop('name', {'age': 21}))        # None
    print(set_prop('age', 24, {'age': 11}))     # {'age': 24}
    print(prop_equals(10, 'age', {'age': 10}))  # True
