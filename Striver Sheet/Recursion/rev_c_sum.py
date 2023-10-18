from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set() 
        candidates.sort()
        temp = []
        def helper(target, ind):
            if target==0:
                res.add(tuple(temp))
                return
            if target < 0 or ind>=len(candidates):
                return
            for index in range(ind, len(candidates)):
                temp.append(candidates[index])
                helper(target-candidates[index], index)
                temp.pop()
        helper(target, 0) 
        return list(res)

sol = Solution()

arr = [2,5,2,1,2]
psum = 8

print(sol.combinationSum(arr, psum))