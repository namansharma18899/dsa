def fun(args):
    for each in args:
        print(recur(each))
    return args

def recur(st: str,curr):
    mp = len(st)
    if curr==mp:
        return 
    # if len(st)%2==0:
    # else:
    #     mp=len(st)/2


if __name__=='__main__':
    print(fun(input().split(',')))