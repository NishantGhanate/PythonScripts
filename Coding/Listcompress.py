"""
@Author : Nishant Ghanate
@Created : 21-10-19 
"""
numbers = [1,1,1,1,1]

def compress(numbers,i):
    while i < len(numbers)-1:
        if numbers[i] == numbers[i+1]:
            numbers[i] = numbers[i] + 1
            del numbers[i+1]
            i = 0
        else:
            i = i+1
            compress(numbers,i)
    return numbers

ans = compress(numbers,i=0)
print(ans)