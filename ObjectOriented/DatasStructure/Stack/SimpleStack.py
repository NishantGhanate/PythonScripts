
stack = []
n = int(input())
for i in range(n):
    stack.append(int(input()))

print('Stack = {}'.format(stack))

print('Stack top = {}'.format(stack[-1]))

print('Stack bottom = {}'.format(stack[0]))

p = int(input("Enter number of elements to pop : "))
for i in range(p):
    print('Elements popped = {}'.format( stack.pop() ))

print('Stack  = {}'.format(stack))

