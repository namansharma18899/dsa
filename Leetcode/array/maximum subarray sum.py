def fun(arr):
    sum =arr[0]
    mx =-88
    for index in range(1, len(arr)):
        sum=max(arr[index], sum+arr[index])
        mx=sum if sum > mx else mx
    return mx


if __name__=='__main__':
    tcs = int(input())
    while(tcs>0):
        print('res -> ', fun([int(x) for x in input().split(' ')]))
        tcs-=1