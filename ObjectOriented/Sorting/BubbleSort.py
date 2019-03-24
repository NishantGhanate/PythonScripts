
def bubble_sort(array,n):
    temp = None
    for k in range (n):
        for i in range (n-k-1):
            if array[i] > array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
    print(array)

array = [7,8,6,9,4,5,1,2,3]
bubble_sort(array,len(array))