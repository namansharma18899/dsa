#from utils import *


def fun(temperatures):
    stack = list()
    stack.append([temperatures[0],0])
    index = 1
    res=[0]*len(temperatures)
    # import pdb;pdb.set_trace()
    while(index<len(temperatures)):
        curr = temperatures[index]
        while(len(stack)>0 and int(stack[len(stack)-1][0])<curr):
            el = stack.pop()
            #print(f'[{el},{curr}]')
            #print(el, stack)
            res[int(el[1])]=index-(int(el[1]))
            #we'll do the adding later
        stack.append([curr,index])
        index+=1
    return res


if __name__=='__main__':
    print(fun(input().split(',')))