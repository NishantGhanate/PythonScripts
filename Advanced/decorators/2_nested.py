"""
Here's the example of nested function aka decorators.
if you can guess the ouput you can guess the order of execution.
"""

def a(wrapped_func):

    def inner(*args, **kwargs):
        print('A')
        wrapped_func()
    return inner

def b(wrapped_func):

    def inner(*args, **kwargs):
        print('B')
        wrapped_func('C')
    return inner


@a
@b
def c(c=None):
    print(c)


c()