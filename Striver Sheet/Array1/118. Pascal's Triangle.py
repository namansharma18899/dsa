#from utils import *

from ast import List


class Solution:
    def generate(self, numRows: int):#-> List[List[int]]:
        # if numRows==0:
        #     return [1]
        res=[[1]]
        previous = [1]
        while(numRows-1>0):
            temp = []
            for index in range(1,len(previous)):
                print('here')
                temp.append(previous[index]+previous[index-1])
            previous = [1]+temp+[1]
            res.append(previous)
            numRows-=1
        return res

def fun(args):
    sol = Solution()
    return sol.generate(args)


if __name__=='__main__':
    print(fun(int(input())))