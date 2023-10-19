from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        stack = []
        outupt = []
        candidates.sort()

        def backtrack(index, total=0):
            if index>=len(candidates) or total > target:
                return
            if total==target:
                outupt.append(stack.copy())
                return
            stack.append(candidates[index])
            backtrack(index+1, total+candidates[index])
            stack.pop()
            """
            When want to stop the recursive tree branch which starts off with same element cand[index] and goes the same path
            So we skip similar elements just to skip those repetitive subtrees
            """
            while(index+1 < len(candidates) and candidates[index]==candidates[index+1]):
                index+=1
            backtrack(index+1, total)
        backtrack(0)
        return outupt


sol = Solution()
arr =[10,1,2,7,6,1,5]
target =8 

print(sol.combinationSum2(arr, target))