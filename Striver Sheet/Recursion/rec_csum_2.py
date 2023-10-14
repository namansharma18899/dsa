from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = set()
        self.comb([], target, 0, 0)
        return [x for x in self.res] 
    
    def comb(self, arr, target, psum, index):
        if psum==target:
            self.res

        