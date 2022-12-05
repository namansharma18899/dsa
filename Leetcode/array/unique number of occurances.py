def fun(args):
    args = [int(x) for x in args]
    res = {}
    for each in args:
        if each not in res.keys():
            res[each]=1
        else:
            res[each]+=1
    counts = [frequency for key, frequency in res.items()]
    if len(counts)==len(set(counts)):
        return True
    return False
    # return args


if __name__=='__main__':
    print(fun(input().split(',')))