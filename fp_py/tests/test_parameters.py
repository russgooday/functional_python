import pytest
from fp_py.internals._parameters import Parameters

def add(a, b, c=2):
    return a + b + c

def function_with_args(a, *args):
    return a + sum(args)

def function_with_kwargs(a, **kwargs):
    return a + kwargs.get('b', 0)

class ClassExample:
    def __init__(self, a, b=1):
        self.a = a
        self.b = b

def test_custom_function():
    parameters = Parameters(add)
    assert parameters.parameters == ('a', 'b', 'c=2')
    assert parameters.paramcount == {
        'self': 0, 'positional': 2, 'default': 1, 'args': 0, 'kwargs': 0
    }

def test_builtin_function():
    parameters = Parameters(str.replace)
    assert parameters.parameters == ('$self', 'old', 'new', 'count=-1')
    assert parameters.paramcount == {
        'self': 1, 'positional': 2, 'default': 1, 'args': 0, 'kwargs': 0
    }

def test_function_with_args():
    parameters = Parameters(function_with_args)
    assert parameters.parameters == ('a', '*args')
    assert parameters.paramcount == {
        'self': 0, 'positional': 1, 'default': 0, 'args': 1, 'kwargs': 0
    }

def test_function_with_kwargs():
    parameters = Parameters(function_with_kwargs)
    assert parameters.parameters == ('a', '**kwargs')
    assert parameters.paramcount == {
        'self': 0, 'positional': 1, 'default': 0, 'args': 0, 'kwargs': 1
    }

def test_lambda_function():
    parameters = Parameters(lambda a, b=1: a + b)
    assert parameters.parameters == ('a', 'b=1')
    assert parameters.paramcount == {
        'self': 0, 'positional': 1, 'default': 1, 'args': 0, 'kwargs': 0
    }

def test_class():
    ''' classes are not currently supported '''
    with pytest.raises(ValueError) as excinfo:
        Parameters(ClassExample)
    assert "Function must have a valid text signature or code object" in str(excinfo.value)


# Running the tests
if __name__ == "__main__":
    pytest.main()
