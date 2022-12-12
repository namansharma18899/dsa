# from utils import *


def fun(grid,cols):
    for index, row in enumerate(grid):
        grid[index] = sorted(row,reverse=True)
    result = 0
    while(cols>0):
        temp = []
        # print(grid)
        for index in range(0,len(grid)):
            # print(grid[index])
            temp.append(grid[index].pop(0))
        result+=max(temp) if len(temp)>0 else 0
        cols-=1
    return result


if __name__=='__main__':
    rows = int(input())
    cols = int(input())
    arr = []
    for i in range(0, rows):
        arr.append([int(inp) for inp in input().split(',')])
    print(fun(arr,cols))