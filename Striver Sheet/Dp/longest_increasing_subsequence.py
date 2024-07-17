arr = [10,9,2,5,3,7,101,18]
from typing import List



class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        self.mem_dp_arr = [None for _ in range(len(nums))]
        def find_lis(nums, index):
            if not self.mem_dp_arr[index]:
                pass
        return 0

