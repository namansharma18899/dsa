def fun(args):
    return perm(args)

def perm(args):
    res = []
    print(sorted(list(set(recur(len(args),[x for x in args], "")))))

def recur(n, el, curr):
    if n == len(curr):
        return curr
    res = []
    ind = 0
    for i in range(0,len(el)):
        temp = []+(el)
        element = el[i]
        popped = temp.pop(i)
        r = recur(n,temp,curr+popped)
        if type(r) == str:
            res.append(r)
        else:
            res= res+r
    return res

if __name__=='__main__':
    print(fun(input()))