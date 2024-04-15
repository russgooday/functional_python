''' WIP - Box Functor for chaining methods '''
class Box:
    '''
    functor for chaining methods

    example usage:
    def square(x): return x ** 2

    def double(x): return x * 2

    (
        Box(5)
            .map(square)        # new Box { x: 25, def map(self, fn).... }
            .inspect('Squared') # 'Squared: 25'
            .fold(double)       # 50
    )
    '''
    def __init__(self, x):
        self.x = x

    def map(self, fn):
        '''returns a new box with the transformed value'''
        return Box(fn(self.x))

    def fold(self, fn):
        '''returns the transformed value'''
        return fn(self.x)

    def inspect(self, message: str):
        '''allows us to inspect values anywhere in the chain'''
        print(f'{message}: {self.x}')
        return Box(self.x)
