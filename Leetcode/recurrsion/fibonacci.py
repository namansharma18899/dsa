def fun(args):
    return fib(args)

def fib(n: int):
    if n<=0:
        return 0
    if n==1:
        return 1
    if n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)+fib(n-3)


if __name__=='__main__':
    print(fun(int(input())))