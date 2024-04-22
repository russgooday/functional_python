'''
    This module is used to get the parameters of a function.
    Currently handles functions with text signatures or code objects.

    Example with custom function:
    def add(a, b, c=2):
        return a + b + c

    print(Parameters(add).parameters)
    # ('a', 'b', 'c=2')
    print(Parameters(add).paramcount)
    # {'self': 0, 'positional': 2, 'default': 1, 'args': 0, 'kwargs': 0}

    Example with built-in function:
    print(Parameters(str.replace).parameters)
    # ('old', 'new', 'count=-1')
    print(Parameters(str.replace).paramcount)
    # {'self': 0, 'positional': 2, 'default': 1, 'args': 0, 'kwargs': 0}
'''

import re

OPTIMIZED = 0x1
NEWLOCALS = 0x2
VARARGS = 0x4
VARKEYWORDS = 0x8

_signature_regexes = {
    'self': r'\$(?P<self>self)',
    'kwargs': r'\*{2}(?P<kwargs>\w+)',
    'args': r'\*(?P<args>\w+)',
    'default': r'(?P<default>\w+)=[^,]+',
    'positional': r'(?P<positional>(?:\b\w+\b))',
}

_signature_regex = re.compile('|'.join(_signature_regexes.values()), flags=re.I)

def _has_text_signature(fn: callable) -> bool:
    '''
    Checks if the given function has a text signature
    '''
    return hasattr(fn, '__text_signature__') and fn.__text_signature__ is not None

def _get_signature_count(text_signature):
    '''
    Parses the text signature and returns the number of each parameter type
    '''
    found_params = {'self': 0, 'positional': 0, 'default': 0, 'args': 0, 'kwargs': 0 }

    matches = re.finditer(_signature_regex, text_signature)

    for match in matches:
        for name, value in match.groupdict().items():
            if value:
                found_params[name] += 1

    return found_params

def _has_code(fn: callable) -> bool:
    '''
    Checks if the given function has a code object
    '''
    return hasattr(fn, '__code__')

def _get_code_count(fn: callable)->dict:

    found_params = {'self': 0, 'positional': 0, 'default': 0, 'args': 0, 'kwargs': 0 }
    code = fn.__code__

    num_params = code.co_argcount
    param_names = code.co_varnames
    num_defaults = len(fn.__defaults__ or ())

    if '$self' in param_names:
        found_params['self'] = 1
        num_params -= 1

    if num_defaults:
        found_params['default'] = num_defaults
        num_params -= num_defaults

    if code.co_flags & VARARGS:
        found_params['args'] = 1

    if code.co_flags & VARKEYWORDS:
        found_params['kwargs'] = 1

    found_params['positional'] = num_params

    return found_params

def _params_count(fn: callable)->dict:
    if _has_text_signature(fn):
        return _get_signature_count(fn.__text_signature__)

    if _has_code(fn):
        return _get_code_count(fn)

    raise ValueError('Function must have a text signature or code object')

def _get_code_signature(fn: callable):

    code = fn.__code__

    num_params = code.co_argcount
    param_names = code.co_varnames
    num_defaults = len(fn.__defaults__ or ())
    positionals = num_params - num_defaults

    params = []

    for i, name in enumerate(param_names[:num_params]):
        if i < positionals:
            params.append(name if name != 'self' else '$self')
        else:
            params.append(f'{name}={fn.__defaults__[i - positionals]}')

    if code.co_flags & VARARGS:
        params.append(f'*{param_names[num_params]}')
        num_params += 1

    if code.co_flags & VARKEYWORDS:
        params.append(f'**{param_names[num_params]}')

    return tuple(params)


def _get_signature(fn: callable)->tuple:
    if _has_text_signature(fn):
        signature = fn.__text_signature__

        return tuple(m.group() for m in re.finditer(_signature_regex, signature))

    if _has_code(fn):
        return _get_code_signature(fn)

    raise ValueError('Function must have a text signature or code object')

def _adjust_params_count(fn: callable) -> callable:
    '''
    Creates a wrapper function that calls the given function with
    the correct number of arguments. Insufficent arguments will still raise an error.

    :param fn: the callback function

    :return: a function that calls the callback
    with the correct number of arguments
    '''
    if not callable(fn):
        raise TypeError('fn must be a callable')

    # wraps the function to ignore extra arguments
    return lambda *args: fn(*args[:Parameters(fn).non_defaults])


class Parameters:
    ''' Returns the parameters of a function '''
    def __init__(self, fn: callable):
        if not callable(fn):
            raise TypeError('fn must be a callable')

        if not _has_text_signature(fn) and not _has_code(fn):
            raise ValueError('Function must have a valid text signature or code object')

        self.paramcount = _params_count(fn)
        self.parameters = _get_signature(fn)

    @property
    def positionals(self):
        ''' Returns the number of positional parameters '''
        return self.paramcount['positional']

    @property
    def defaults(self):
        ''' Returns the number of default parameters '''
        return self.paramcount['default']

    @property
    def self(self):
        ''' Returns the number of self parameters '''
        return self.paramcount['self']

    @property
    def non_defaults(self):
        ''' Returns the number of non-default parameters '''
        return self.self + self.positionals - self.defaults
