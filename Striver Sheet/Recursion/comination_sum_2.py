#from utils import *

from ast import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = self.comb(sorted(candidates), target, 0, [])
        return res
    
    def comb(self, nums, target, index, result):
        if index>=len(nums):
            return result
        res = []
        result.append(nums[index])
        for index in range(index, len(nums)):
            temp_res = self.comb(nums, target-nums[index], index+1, result)


def fun(args):
    sol = Solution()
    return sol.fun(args)


if __name__=='__main__':
    print(fun(input().split(',')))