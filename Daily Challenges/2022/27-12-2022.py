#from utils import *
from math import ceil,floor
from collections import defaultdict
#TODO: COULDN'T SOLVE

class Solution:
    def minStoneSum(self, piles, k: int) -> int:
        sum = 0
        #hashmap for different len of piles
        heights= defaultdict(list)
        for index, each in enumerate(piles):
            heights[each].append(index)
            sum+=each
        piles= sorted(piles, reverse=True)
        

def fun(args):
    sol=Solution()
    return sol.minStoneSum([int(x) for x in args], int(input()))


if __name__=='__main__':
    print(fun(input().split(',')))