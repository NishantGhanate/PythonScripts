"""
Calling excution :
1 - calling sqaure
2 - calling add
3 - Adding value : 6, 9
4 - Result 15
5 -Squaring : 15
6 - Result 225
7- Value returned = 225
"""

def add(wrapped_func):
    print('calling add')
    def inner(*args, **kwargs):
        c = args[0] + args[1]
        print('Adding value : {}, {}'.format(args[0], args[1]))
        print('Result {}'.format(c))
        return wrapped_func(c)
    return inner

def sqaure(wrapped_func):
    print('calling sqaure')
    def inner(*args, **kwargs):
        c = args[0] ** 2
        print('Squaring : {}'.format(args[0]))
        print('Result {}'.format(c))
        return c
    return inner


@add
@sqaure
def maths_on_numners(a= None, b = None):
    pass

a, b = 6, 9
value = maths_on_numners(a, b)
out_msg = 'Value returned = {value}'
print(out_msg.format(value = value))