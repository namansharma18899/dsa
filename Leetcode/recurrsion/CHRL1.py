def fun(n,k,w,p):
    max = 1000000
    return max
    # return args


if __name__=='__main__':
    tcs = int(input())
    while(tcs>0):
        inp = input().split(' ')
        n,k = int(inp[0]),int(inp[1])
        wieghts, price = [],[]
        for i in range(0,k):
            inp = input().split(' ')
            wieghts[i],price[i] = int(inp[0]),int(inp[1])
        print(fun(n, k, wieghts, price))




