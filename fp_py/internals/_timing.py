''' Timing decorator for functions'''
# https://stackoverflow.com/questions/1622943/timeit-versus-timing-decorator
# credit Jonathan Prieto-Cubides
from functools import wraps
from time import time

def _timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print(f'func:{f.__name__} args:{args} took: {te-ts:.4f} sec')
        return result
    return wrap
