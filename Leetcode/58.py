def fun(args):
    s = args.strip()
    return s.split(' ')[::-1][0]


if __name__=='__main__':
    print(fun(input()))