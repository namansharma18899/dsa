import itertools
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = []
        N = len(nums)
        res = []
        curr_sol = []
        def perm_helper():
            if len(curr_sol)==N: # find sol
                temp = curr_sol+[]
                res.append(temp)
                return
            rem_len = len(curr_sol)
            while(rem_len< N):
                el = nums.pop(0)
                curr_sol.append(el)
                perm_helper()
                curr_sol.pop()
                nums.append(el)
                rem_len+=1

        for _ in range(N):
            el = nums.pop(0)
            curr_sol.append(el)
            perm_helper()
            curr_sol.pop()
            nums.append(el)
        return res

nums = [1,2,3]
sol = Solution()
print(sol.permute(nums))