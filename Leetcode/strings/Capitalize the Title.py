#from utils import *
from functools import reduce

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        result = []
        for each in title.split(' '):
            if len(each)<=2:
                result.append(each.lower())
            else:
                result.append(each[0].upper()+each[1:].lower())
        return reduce(lambda a, b : a+ " " +str(b), result)

def fun(args):
    sol = Solution()
    return sol.capitalizeTitle(args)


if __name__=='__main__':
    print(fun(input().split(' ')))