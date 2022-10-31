def fun(args):
    n1 = int(args[0])
    n2 = int(args[1])
    for index in range(min(n1,n2), -1, -1):
        if n1%index==0 and n2%index==0:
            return index


if __name__=='__main__':
    print(fun(input().split(',')))