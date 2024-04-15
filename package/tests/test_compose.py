import pytest
from package.internals._compose import _compose, _pipe, _compose_two, _compose_three

def indentity(x):
    return x

def add(x, y):
    return x + y

def square(x):
    return x ** 2

def halve(x):
    return x * 0.5

def double(x):
    return x * 2

def triple(x):
    return x * 3

def inc(x):
    return x + 1

def test_compose():
    # composition law test
    assert _compose(indentity, square)(5) == 25

    # Test case with 1 function
    assert _compose(square)(5) == 25

    # Test case with 2 functions
    assert _compose_two(square, double)(5) == 100

    # Test case with 3 functions
    assert _compose_three(square, double, inc)(5) == 144

    # Test case with 4 functions
    assert _compose(square, double, inc, add)(5, 2) == 256

def test_compose_associative():
    # f(g(h(x)))
    composed1 = halve(triple(double(10)))

    # (f ◦ g)(h(x))
    composed2 = _compose(halve, triple, double)(10)

    # (g ◦ h)(f(x))
    composed3 = _compose(triple, halve, double)(10)

    # f(g(h(x))) == (f ◦ g)(h(x)) == (g ◦ h)(f(x))
    assert composed1 == composed2 == composed3

def test_pipe():
    # composition law test
    assert _pipe(indentity, square)(5) == 25

    # Test case with 1 function
    assert _pipe(square)(5) == 25

    # Test case with 2 functions
    assert _pipe(square, double)(5) == 50

    # Test case with 3 functions
    assert _pipe(square, double, inc)(5) == 51

    # Test case with 4 functions
    assert _pipe(add, square, inc, double)(5, 2) == 100

    # Test case with too many arguments for the first function
    with pytest.raises(TypeError) as excinfo:
        _pipe(square, double, inc, add)(5, 2)
    assert 'square() takes 1 positional argument but 2 were given' in str(excinfo.value)

def test_pipe_associative():
    # f(g(h(x)))
    piped1 = halve(triple(double(10)))

    # (f ◦ g)(h(x))
    piped2 = _pipe(halve, triple, double)(10)

    # (g ◦ h)(f(x))
    piped3 = _pipe(triple, halve, double)(10)

    # f(g(h(x))) == (f ◦ g)(h(x)) == (g ◦ h)(f(x))
    assert piped1 == piped2 == piped3

# Running the tests
if __name__ == "__main__":
    pytest.main()