def fun(arr):
    res = []
    arr = [int(x) for x in arr]
    lmax, rmax = (len(arr))*[-1],(len(arr))*[-1]
    mx = arr[0]
    # print(lmax, rmax)
    for index in range(1, len(arr)):
        if arr[index] > arr[mx]:
            mx=index
        # print(index, mx)
        lmax[index] = mx
    index = len(arr)-1
    mx=arr[-1]
    while(index>=0):
        if arr[index]>mx:
            mx=arr[index]
        rmax[index]=mx
        index-=1
    water = 0
    for index in range(1, len(arr)-1):
        water+= (min(lmax[index], rmax[index]) - arr[index]) if (min(lmax[index], rmax[index]) > arr[index]) else 0
    return water

if __name__=='__main__':
    tcs = int(input())
    while(tcs>0):
        print('RES -> ', fun(input().split(' ')))
        tcs-=1