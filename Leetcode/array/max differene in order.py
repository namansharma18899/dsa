def fun(arr):
    arr = [int(x) for x in arr]
    lmax, max = -99, -9999
    index = len(arr)-1
    while(index>=0):
        if arr[index]>max:
            max=arr[index]
        if max-arr[index]>lmax:
            lmax=max-arr[index]
        index-=1
    return lmax


if __name__=='__main__':
    tcs = int(input())
    while(tcs>0):
        arr = input().split(' ')
        print(fun(arr))
        tcs-=1