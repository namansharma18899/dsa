import math
def check_palindrome(num):
    return True if str(num)==str(num)[::-1] else False

def palin(args):
    intLength = int(input())
    if intLength%2==0:
        pairs= int(math.pow(10,int(intLength/2)-1))
        power= int(intLength/2)-1
    else:
        power = int(intLength/2)
        pairs = (int(math.pow(10,int(intLength/2))))
    res = list()
    defaults = []
    len = intLength
    while(len>0):
        if len>1:
            defaults.append(1*int(math.pow(10,len-1))+1)
        else:
            defaults.append(0)
        len-=2
    print(defaults)
    for each in args:
        res.append(recur(each,defaults))
    return 1

def recur(n, p, default):

    pass

def fun(args):
    intLength = int(input())
    r1 = int(math.pow(10,intLength-1))
    args = [int(x) for x in args]
    palins = []
    #compute in runtime
    # for each in args:
    #     posi = each/(math.pow(10,intLength-1))

    for index in range(r1, r1*10):
        # print(index)
        if check_palindrome(index):
            palins.append(index)
    result = []
    print(palins[-1])
    print(len(palins))
    for each in args:
        if each <= len(palins):
            print(each, len(palins))
            result.append(palins[each-1])
    return result


if __name__=='__main__':
    print(palin(input().split(',')))