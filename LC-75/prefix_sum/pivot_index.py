from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n2 = 0
        sm = sum(nums)
        for index, each  in enumerate(nums):
            if sm - (each + n2) == n2:
                return index
            n2+=each
        return -1