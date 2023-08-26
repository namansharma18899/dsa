from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        one_count = 0
        for index in range(1, len(nums)):
                if nums[index]==0:
                    continue
                else:
                    nums[index]+=nums[index-1]
        return max(nums)



sol = Solution()

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

print(sol.longestOnes(nums, k))
