def fun(args):
    s = sorted(args)
    min = s[0]+s[1]+s[2]
    for index in range(2,len(s)):
        sum+=s[index]
        if sum<min:
            min = sum
        sum-=

if __name__=='__main__':
    print(fun(input().split(',')))