def summation(*args):
    return sum(args)

def curry(func):
    # to keep the name of the curried function:
    curry.__curried_func_name__ = func.__name__
    f_args, f_kwargs = [], {}
    def f(*args, **kwargs):
        nonlocal f_args, f_kwargs
        if args or kwargs:
            print("Calling curried function with:")
            print("args: ", args, "kwargs: ", kwargs)
            f_args += args
            f_kwargs.update(kwargs)
            print("Currying the values:")
            print("f_args: ", f_args)
            print("f_kwargs:", f_kwargs)
            return f
        else:
            print("Calling " + curry.__curried_func_name__ + " with:")
            print(f_args, f_kwargs)
            result = func(*f_args, *f_kwargs)
            f_args, f_kwargs = [], {}
            return result
    return f



curried_summation = curry(summation)
curried_summation(1)(2)(3)(4, 5)

# it will keep on currying:
# curried_arimean(6, 7)
print(curried_summation())