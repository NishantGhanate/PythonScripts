
# Complete the plusMinus function below.
def plusMinus(arr):
    arr_len = len(arr)
    positive = negative = zero = 0.00
    for i in range(arr_len):
        if arr[i] >0:
            positive = positive + 1
        elif arr[i]<0:
            negative = negative + 1
        else :
            zero = zero + 1
    positive = positive / arr_len
    negative = negative / arr_len
    zero = zero / arr_len

    print('{0:.4f}'.format(positive))
    print('{0:.4f}'.format(negative))
    print('{0:.4f}'.format(zero))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
