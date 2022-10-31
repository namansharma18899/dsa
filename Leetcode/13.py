def fun(args):
    hashmap = {
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000,
    }
    
    return args


if __name__=='__main__':
    print(fun(input().split(',')))