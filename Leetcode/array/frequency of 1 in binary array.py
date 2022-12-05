def fun(arr):
    count = 0
    max = -999
    for index in range(1, len(arr)):
        if arr[index]==1:
            arr[index]+= arr[index-1]
        else:
            if arr[index-1]>max:
                max=arr[index-1]
    return max

if __name__=='__main__':
    tcs = int(input())
    while(tcs>0):
        print('RES -> ', fun([int(x) for x in input().split(' ')]))
        tcs-=1