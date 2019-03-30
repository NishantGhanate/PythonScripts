a = [[11,2,4] , [4,5,6] , [10,8,-12]]
n = len(a)

diagonal_1 = diagonal_2 = 0


for i,j in zip(range(0,n), range(n-1,-1,-1)):
    #print("i={},j={}".format(i,j))
    #print(a[i][i])
    #print(a[i][j])
    diagonal_1 = diagonal_1 + a[i][i]
    diagonal_2 = diagonal_2 + a[i][j]
    
print(abs(diagonal_1 - diagonal_2))
#print(diagonal_1)
#print(diagonal_2)
