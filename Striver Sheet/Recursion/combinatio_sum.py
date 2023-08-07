from collections import defaultdict
from typing import List

# from utils import *
"""
INTUTION -> 
premise: number of unique sets of {[a:b], [c:d]}, no two items with same keys have same values
Scenario:

if (len(keys)== same){
    if (set(keys)== same)){
        compare_two_dicts( )
    } 
}
ISSUE -> HOW TO COMPARE MULTIPLE DICTS ???

SOLUTION -> 

LEARNING : we can use loops inside recursive code.... thus we can achieve ( current + move ahead scenarios )
"""

"""
Personal Try
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.find_com([] + sorted(candidates), target, 0)

    def find_com(self, nums, target, index, curr):
        # Edge case
        if target==0:
            return curr
        if target<0:
            return [[]]
        res = [[]]
        for i in range(index, len(nums)):
            temp = []+curr+nums[index]
            res_i = self.find_com(nums, target-nums[index],temp) #[[2,3],[5]] -> [[6,-1]]``
            if res_i!=[[]]:
                res+=res_i
        return res
            

    # def find_com(self, nums, target, index, curr_sum, curr_dict=defaultdict(int)):
    #     # +ve passed
    #     # boundary
    #     if index >= len(nums):
    #         return curr_dict if curr_sum == target else [{}]
    #     if nums[index] > target:
    #         return [{}]
    #     res = []
    #     # Skip this
    #     res1 = self.find_com(nums, target, index + 1, curr_sum, curr_dict)
    #     curr_dict[nums[index]] += 1
    #     curr_sum += nums[index]
    #     # incld this and move on
    #     res2 = self.find_com(nums, target, index + 1, curr_sum, curr_dict)
    #     # incld this again
    #     res3 = self.find_com(nums, target, index, curr_sum, curr_dict)
    #     """Now filter the duplicate ones out"""

def fun(args):
    sol = Solution()
    return sol.fun(args)


if __name__ == "__main__":
    print(fun(input().split(",")))
