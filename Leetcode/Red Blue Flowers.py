class Obj:
    def __init__(self,a,b):
        self.a=a
        self.b=b

def fun(ln,r,b):
    s1,s2=0,0
    Objs = [Obj(r[i],b[i]) for i in range(0,ln)]
    for index in range(0,ln):
        s1+=r[index]
        s2+=b[index]
    min = 999999
    for 


if __name__=='__main__':
    tcs = int(input())
    while(tcs>0):
        inp = int(input())
        r = input().split(' ')
        b = input().split(' ')
        # a,b,c = int(inp[0]), int(inp[1]), int(inp[2])
        print(fun(inp, r,b))
        tcs-=1