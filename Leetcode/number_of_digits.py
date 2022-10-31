
def fun(args):
    from math import log10, log
    print(int(log(int(args))))
    print(int(log10(int(args)))+1)


if __name__=='__main__':
    print(fun(input()))