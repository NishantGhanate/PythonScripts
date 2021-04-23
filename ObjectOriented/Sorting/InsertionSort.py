def insertion_sort(array,n):
    for i in range(n):   
    # sorting current element whose left side is checked for its 
    # correct position
        temp = array[i]
        j = i   
        # check whether the adjacent element in left side is greater or
        # less than the current element. 
        while j > 0 and temp < array[j-1]:
            # moving the left side element to one right
            array[j] = array[j-1]
            j = j -1
        array[j] = temp
    return array

array = [7,8,9,4,5,6,1,2,3]
array = insertion_sort(array,len(array))
print(array)  

