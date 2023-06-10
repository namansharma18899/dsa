#from utils import *


from functools import lru_cache


class Solution:
    # @lru_cache
    def reversePairs(self, nums):# List[int]) -> int:
        """
        I must widen my horizon, it is a giant input...
        Intuition -> dp array for pair, dp[j]+=2*dp[i] if reversepair(i,j)
        5 4 3 2 1
        2,1 -> min_sq = [(2,0),(4,1)] *could be a heap...
        direction of thought ->>>>> ....
        """
        mx = max(nums)
        aux = [0]*((mx**2)+1)
        for each in nums:
            aux[each]=1
        prev = aux[-1]
        for index in range(len(aux)-1,-1,-1):
            if aux[index]!=0:
                prev+=1
                aux[index]=prev
        res = 0
        for each in nums:
            res+=aux[each]-1
        return res
        


def fun(args):
    sol = Solution()
    return sol.reversePairs([int(x) for x in args])


if __name__=='__main__':
    print(fun(input().split(',')))