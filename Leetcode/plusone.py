def fun(digits):
    res=''
    ad = 1
    flag = False
    while(digits):
        el = int(digits.pop())
        el+=int(ad)
        if el / 10 >= 1:
            res+='0'
        else:
            res+=str(el)
            flag=True
            break
    print(res)
    return int(res[::-1])


if __name__=='__main__':
    print(fun(input().split(',')))