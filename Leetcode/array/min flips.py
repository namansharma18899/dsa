def fun(args):
    args = [int(x) for x in args]
    o, z = 1 if args[-1]==1 else 0,1 if args[-1]==0 else 0
    for index in range(0,len(args)-1):
        if args[index]!=args[index+1]:
            if args[index+1]==0:
                z+=1
            else:
                o+=1
    for index in range(0,len(args)-1):
        if args[index]==0:
            if index!=0 and args[index+1]==0 and args[index-1]==0:
                pass
            else:
                print(index)
    if args[-1]==0:
        print(len(args)-1)

if __name__=='__main__':
    print(fun(input().split(' ')))

#1 0 0 0 1 0 0 1 1 1