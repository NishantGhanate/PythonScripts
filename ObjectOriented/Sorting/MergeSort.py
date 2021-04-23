class MergeSort:
    def __init__(self,array):
        self.merge_sort(array)

    def merge_sort(self,array):
        print("\nGiven List = {} ".format(array))
        if len(array)>1:
            mid = len(array)//2
            print("Mid index = {} ".format(mid))

            # From 0 till mid index
            left_half = array[:mid]
            print("Left half = {} ".format(left_half))

            # From mid till end index
            right_half = array[mid:]
            print("Right half = {} ".format(right_half))
            
            self.merge_sort(left_half)
            self.merge_sort(right_half)

            i = 0
            j = 0
            k = 0

            while i < len(left_half) and j < len (right_half):
                if left_half[i] < right_half[j]:
                    array[k] = left_half[i]
                    i = i + 1
                else:
                    array[k] = right_half[j]
                    j = j + 1
                k = k +1
            
            while i < len (left_half):
                array[k] = left_half[i]
                i = i + 1
                k = k + 1
            
            while j < len (right_half):
                array[k] = right_half[j]
                j = j +1
                k = k + 1
        print("Merging ",array)

if __name__ =="__main__":
    array = [9,5,4,8,6,7,3,1,2]
    MergeSort(array)


# Given List = [9, 5, 4, 8, 6, 7, 3, 1, 2]
# Mid index = 4
# Left half = [9, 5, 4, 8]
# Right half = [6, 7, 3, 1, 2]

# Given List = [9, 5, 4, 8]
# Mid index = 2
# Left half = [9, 5]
# Right half = [4, 8]

# Given List = [9, 5]
# Mid index = 1
# Left half = [9]
# Right half = [5]

# Given List = [9]
# Merging  [9]

# Given List = [5]
# Merging  [5]
# Merging  [5, 9]

# Given List = [4, 8]
# Mid index = 1
# Left half = [4]
# Right half = [8]

# Given List = [4]
# Merging  [4]

# Given List = [8]
# Merging  [8]
# Merging  [4, 8]
# Merging  [4, 5, 8, 9]

# Given List = [6, 7, 3, 1, 2]
# Mid index = 2
# Left half = [6, 7]
# Right half = [3, 1, 2]

# Given List = [6, 7]
# Mid index = 1
# Left half = [6]
# Right half = [7]

# Given List = [6]
# Merging  [6]

# Given List = [7]
# Merging  [7]
# Merging  [6, 7]

# Given List = [3, 1, 2]
# Mid index = 1
# Left half = [3]
# Right half = [1, 2]

# Given List = [3]
# Merging  [3]

# Given List = [1, 2]
# Mid index = 1
# Left half = [1]
# Right half = [2]

# Given List = [1]
# Merging  [1]

# Given List = [2]
# Merging  [2]
# Merging  [1, 2]
# Merging  [1, 2, 3]
# Merging  [1, 2, 3, 6, 7]
# Merging  [1, 2, 3, 4, 5, 6, 7, 8, 9]