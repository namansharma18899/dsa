def fun(args):
    return recur(args[0],"",0)
    # return args

def recur(org,st,index):
    #base case
    if index==len(org):
        print(st)
        return
    #choices
    #to choose the ith element or skip in sbsqnce
    recur(org,st,index+1)#skip
    st=st+org[index]
    recur(org,st,index+1)#inc

if __name__=='__main__':
    print(fun(input().split))