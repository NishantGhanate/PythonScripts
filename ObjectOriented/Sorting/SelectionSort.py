def selection_sort(array , n):
    minimum = None
    for i in range(n-1):
        # assume first elemnt is lowest
        minimum = i
        for j in range(i+1,n):
            if array[j] < array[minimum]:
                minimum = j
        # Swap the found minimum element with  
        # the first element         
        array[i], array[minimum] = array[minimum], array[i] 
    return array

array = [7,8,9,4,5,6,1,2,3]
array = selection_sort(array,len(array))
print(array)
