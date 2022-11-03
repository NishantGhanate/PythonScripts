def func1(func):
    def inner(*args, **kwd):
        val = sum(args)
        return func(val, **kwd)
    return inner


def func2(func):
    def inner(*agrs, **kwd):
        # print(agrs, type(kwd['c']['c_key']))
        total = agrs[0] + kwd['c']['c_key']
        kwd = {}
        return func(total, kwd)
    return inner

@func1
@func2
def something(*args, **kwd):
    # print(args, kwd)
    return args[0]


ans = something(1, 2, c= {'c_key': 3})
print(ans)