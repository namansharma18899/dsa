def fun(arr):
    arr = [int(x) for x in arr]
    lmax, max = [], -9999
    index = len(arr)-1
    while(index>=0):
        if arr[index]>max:
            max=arr[index]
            lmax.append(max)
        index-=1
    return lmax[::-1]


if __name__=='__main__':
    tcs = int(input())
    while(tcs>0):
        arr = input().split(' ')
        print(fun(arr))
        tcs-=1