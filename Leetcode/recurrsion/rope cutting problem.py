def fun(args):
    n = int(input())
    args = [int(x) for x in args]
    return recur(n, args,n)
    # return args


def recur(n, elemsnts,curr):
    if n <= 0 or curr<0:
        return -1
    if curr==0:
        return 1
    res = []
    for each in elemsnts:
        if curr-int(each)>=0:
            rec = int((recur(n,elemsnts,curr-int(each))))
            if curr==n:
                res.append(rec)
            else:
                res.append(rec+1 if rec>=1 else rec)
    max = -1
    print('res ->',res)
    for each in res:
        if each > max:
            max=each
    return max

if __name__=='__main__':
    print(fun(input().split(',')))
