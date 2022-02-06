import time

cached = {}

def memo(wrapped_func):
    def inner(n1, n2):
        params = '{}{}'.format(n1, n2)
        if params not in cached:
            value = wrapped_func(n1, n2)
            cached[params] = value
            return value
        return cached[params]
    return inner

@memo
def calucate_sum(n1, n2):
    _sum = 0
    for i in range(n1, n2):
        _sum += i
    return _sum

start = time.time()
value = calucate_sum(1, 100000000)
end = time.time()
total_time = end - start
print('Before memo')
print('Value = {}, total time = {}'.format(value, total_time))

start = time.time()
value = calucate_sum(1, 100000000)
end = time.time()
total_time = end - start
print('\nAfter memo')
print('Value = {}, total time = {}'.format(value, total_time))