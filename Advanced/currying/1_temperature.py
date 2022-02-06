# source : https://python-course.eu/advanced-python/currying-in-python.php

# h(x) = g(f(x))

def compose(g, f):
    def h(x):
        return g(f(x))
    return h

def celsius_fahrenheit(t):
    return 1.8 * t + 32

def correct_error(t):
    return 0.9 * t - 0.5


convert = compose(correct_error, celsius_fahrenheit)
print(convert(10), celsius_fahrenheit(10))