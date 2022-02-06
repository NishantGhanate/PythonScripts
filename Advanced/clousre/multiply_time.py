
def multiply(x):
    def inner(n):
        return x * n
    return inner


times_2 = multiply(2)
val = times_2(2)
print(val)