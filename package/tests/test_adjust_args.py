import pytest
from package.internals._args_count import _adjust_args_count

# Sample callback functions


def func1(a, b, c):
    return (a, b, c)


def func2(x, y):
    return (x, y)

# Tests for _adjust_args_count function


def test_adjust_args_count_with_exact_args():
    func = _adjust_args_count(func1)
    assert func(1, 2, 3) == (1, 2, 3)


def test_adjust_args_count_with_insufficient_args():
    func = _adjust_args_count(func1)
    with pytest.raises(TypeError) as excinfo:
        func(1, 2)
    assert 'func1() missing 1 required positional argument: \'c\'' in str(excinfo.value)


def test_adjust_args_count_with_extra_args():
    func = _adjust_args_count(func2)
    assert func(1, 2, 3) == (1, 2)


def test_adjust_args_count_with_no_args():
    func = _adjust_args_count(func1)
    with pytest.raises(TypeError) as excinfo:
        func()
    assert (
        'func1() missing 3 required positional arguments: \'a\', \'b\', and \'c\'' in
        str(excinfo.value)
    )


def test_adjust_args_count_with_non_callable():
    with pytest.raises(TypeError) as excinfo:
        _adjust_args_count((1, 2, 3))
    assert 'fn must be a callable' in str(excinfo.value)


# Running the tests
if __name__ == "__main__":
    pytest.main()
