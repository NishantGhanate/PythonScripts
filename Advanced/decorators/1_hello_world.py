def add_world(wrapped_func):

    def inner_func():
        wrapped_func()
        print('World')
    
    return inner_func

@add_world
def hello():
    print('Hello', end=' ')


hello()