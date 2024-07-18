arr = [10, 9, 2, 5, 3, 7, 101, 18]
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        self.mem = [1 for _ in range(len(nums))]

        def calc_lis(nums, start_index, p_num, index, p_sum):
            if index == len(nums) - 1:
                self.mem[start_index] = max(p_sum, self.mem[start_index])
                return p_sum
                # BASE COND.FOR RECUR
            # Consider this element if increasing or move forward
            if not self.mem[index]:
                pass
            else:
                pass
            calc_lis(nums, start_index, nums[index], index+1, p_sum+1 if nums[index]>p_num else p_sum)
            calc_lis(nums, start_index, p_num, index+1, p_sum)

            # if self.mem[index]:
            # if nums[index] > p_num:
            #     self.mem[start_index] = max(self.mem[start_index], p_sum + 1)
            # else:
            #     self.mem[start_index]
                # return self.mem[index]
        calc_lis(nums, 1, nums[0], 1, 1)
        return max(self.mem)