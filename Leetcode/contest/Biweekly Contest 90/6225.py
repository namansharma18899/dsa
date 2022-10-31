import string
def fun(args):
    kv = {}
    count=0
    wrd = {}
    for each in string.ascii_lowercase:
        wrd[each] = count
        count+=1
    # nums = {alph: count+1}
    res = []
    for each in args:
        d = []
        for index in range(0,len(each)-1):
            d.append(int(wrd[each[index]])-int(wrd[each[index+1]]))
        if len(res==0):            
            res.append(d)
        else:
            if d!=res[-1]:
                return 
    # res = sorted(res)
    # for index in range(0, len(res-1)):
    #     if res[index]!=res[index+1]
    # return args


if __name__=='__main__':
    print(fun(input().split(',')))