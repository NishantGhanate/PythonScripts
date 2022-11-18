from ctypes import CDLL

so_file = r'./functions.so'

functions = CDLL(so_file)

squared = functions.square(10)
print(squared)

my_list = [i for i in range(1,100000)]
even_nums = functions.get_even(my_list)
print(even_nums[0:10])