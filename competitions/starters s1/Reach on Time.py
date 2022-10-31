# def fun(num):
#     if num>=30:
#         return 'YES' 
#     else:
#         return 'NO'
#     pass


# if __name__=='__main__':
#     tcs = int(input())
#     while(tcs>0):
#         num = int(input())
#         print(fun(num))
#         tcs-=1


# cook your dish here
def fun(a,b):
    count =0
    res = ""
    for index in  range(1, a):
        if b[index]==b[index-1]:
            count+=1
    return count
    # if (a+b)%2 !=0:
    #     return 'YES'
    # elif (a+c)%2 !=0:
    #     return 'YES'
    # elif (c+b)%2 !=0:
    #     return 'YES'
    # else:
    #     return 'NO'




if __name__=='__main__':
    tcs = int(input())
    while(tcs>0):
        inp = int(input())
        num = input()
        # a,b,c = int(inp[0]), int(inp[1]), int(inp[2])
        print(fun(inp, num))
        tcs-=1