def fun(arr):
    arr= [int(x) for x in arr]
    profit = 0
    # prev = 0
    for ind in range(1, len(arr)):
        if arr[ind]>arr[ind-1]:
            profit+=arr[ind]-arr[ind-1]
        # prev = ind
    return profit


if __name__=='__main__':
    tcs = int(input())
    while(tcs>0):
        print('RES -> ', fun(input().split(' ')))
        tcs-=1