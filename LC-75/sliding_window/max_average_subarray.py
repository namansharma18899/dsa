from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSum = -999
        window_sum = 0
        for index in range(0, len(nums)):
            if index < k:
                window_sum+=nums[index]
                maxSum = window_sum
                continue
            window_sum  = window_sum - (nums[index - k]) + nums[index]
            maxSum = max(maxSum, window_sum)
        return maxSum/k


sol = Solution()
nums = [1,12,-5,-6,50,3]
k = 4

print(sol.findMaxAverage(nums, k))