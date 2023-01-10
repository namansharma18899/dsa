#from utils import *
    class Solution:
        def maxSubArray(self, nums):# List[int]) -> int:
            prev = nums[0]
            max = nums[0]
            for index in range(1, len(nums)):
                if nums[index]>nums[index]+prev:
                    prev = nums[index]
                else:
                    prev+=nums[index]
                if prev>max:
                    max = prev
            return max

def fun(args):
    sol = Solution()
    return sol.maxSubArray([int(x) for x in args])


if __name__=='__main__':
    print(fun(input().split(',')))