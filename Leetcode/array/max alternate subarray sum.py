def fun(arr):
    arr =[int(x) for x in arr]
    prev = arr[0]
    sum, max = 1, 1
    for index in range(1, len(arr)):
        print(arr[index], sum, max)
        if (arr[index-1]+arr[index])%2!=0:
            sum+=1
            max = sum if sum>max else max
        else:
            sum=1
    return max

if __name__=='__main__':
    tcs = int(input())
    while(tcs>0):
        print('res -> ',fun(input().split(' ')))
        tcs-=1