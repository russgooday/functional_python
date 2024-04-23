from fp_py.prop import get_prop, set_prop
from fp_py.path import get_by_path, set_by_path
from fp_py.internals._curry import _curry_2, _curry_3


class Lens:
    def __init__(self, getter, setter):
        self.get = getter
        self.set = setter


def lensProp(key: str):
    return Lens(get_prop(key), set_prop(key))


def lensPath(path: list):
    return Lens(get_by_path(path), set_by_path(path))


def lensIndex(index: int):
    return Lens(get_prop(index), set_prop(index))


def _view(lens, obj: dict | list):
    return lens.get(obj)


def _set(lens, val: any, obj: dict | list):
    return lens.set(val, obj)


def _over(lens, fn, obj: dict | list):
    return lens.set(fn(lens.get(obj)), obj)


lens_view = _curry_2(_view)

lens_set = _curry_3(_set)

lens_over = _curry_3(_over)

if __name__ == "__main__":
    import json

    # Example usage:

    basic_obj = {'a': 1, 'b': 2, 'c': 3}
    test_user = {'name': 'john paul smith', 'age': 33}

    print(lens_view(lensProp('b'), basic_obj))
    # 2
    print(lens_set(lensProp('b'), 4, basic_obj))
    # {'a': 1, 'b': 4, 'c': 3}
    print(basic_obj)
    # {'a': 1, 'b': 2, 'c': 3}
    print(lens_over(lensProp('name'), str.title, test_user))
    # {'name': 'John Paul Smith', 'age': 33}

    # Example with nested objects:
    characters = [
        {
            'name': 'Fred Flintstone',
            'address': {
                'house_number': 123,
                'street': 'Cobblestone Way',
                'city': 'Bedrock',
                'state': 'CA'
            }
        },
        {
            'name': 'Barney Rubble',
            'address': {
                'house_number': 125,
                'street': 'Cobblestone Way',
                'city': 'Bedrock',
                'state': 'CA'
            }
        }
    ]

    def indent(obj):
        return json.dumps(obj, indent=2)

    print(lens_view(lensPath([0, 'address', 'house_number']), characters))
    # 123
    print(indent(
        lens_set(lensPath([0, 'address', 'house_number']), 124, characters)
    ))
    # [{'name': 'Fred Flintstone', 'address': {'house_number': 124, ...
    print(indent(
        lens_over(lensPath([0, 'name']), str.upper, characters)
    ))
    # [{'name': 'FRED FLINTSTONE', 'address': {'house_number': 123, ...
    print(indent(characters))
    # [{'name': 'Fred Flintstone', 'address': {'house_number': 123, ...
