# arr = [[1, 2], [4, 5]]
# arr2 = [[1,2], [4,5]]
arr = [[1,2,3], [4,5,6]]
arr2 = [[2,3],[1,2],[2,1]]

R1 = len(arr)
C1 = len(arr[0])

R2 = len(arr2)
C2= len(arr2[0])


result = [ ]

def getdot(arr1_row, arr2_col):
    res = 0
    counter = 0
    while(counter < R2):
        res+=arr[arr1_row][counter] * arr2[counter][arr2_col] 
        counter+=1
    return res


for row_index in range(R1):
    temp = []
    for col_index in range(C2):
        temp.append(getdot(row_index, col_index))
    result.append(temp)

print(result)