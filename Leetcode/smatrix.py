def maxSum(grid,n,m):
        #initial thoughts, find all hourglass shapes, sum the elements in them, find the max sum
        sm, max = 0, 0
        k=3
        for i in range(0, n-(k-1)):
            for j in range(0,m-(k-1)):
                print('i,j -> ', i, j)
                # while(k<n):
                sm = sumMatrix(grid, i,j,k)
                print('sm -> ', sm)
                if sm > max:
                    max = sm 
                    # k+=2
        return max
def sumMatrix(grid, ri, ji,k):
    s=0
    # if ji==2:
    #     import pdb; pdb.set_trace()
    for upperHourGlassIndex in range(ji, ji+(k)):
        s+=grid[ri][upperHourGlassIndex]
    for middleHourGlassIndex in range(ri+1, ri+(k-1)):
        s+=grid[middleHourGlassIndex][ji+int((k/2))]
    for lowerHourGlassIndex in range(ji, ji+(k)):
        s+=grid[ri+(k-1)][lowerHourGlassIndex]
    return s


# gr = [[1,2,3],[4,5,6],[7,8,9]] 
gr = [[520626,685427,788912,800638,717251,683428],\
      [23602,608915,697585,957500,154778,209236],\
      [287585,588801,818234,73530,939116,252369]]
# [[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]]
print(maxSum(grid=gr,n=3,m=6))