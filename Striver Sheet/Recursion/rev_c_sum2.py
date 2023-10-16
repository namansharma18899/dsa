from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # self.cands = list(set(candidates))
        self.cands = sorted(candidates)
        self.a_hash = set()
        self.comb(target, [], 0, 0)
        return [x for x in self.a_hash]

    def comb(self, target,arr, psum, index):
        if psum>target:
            return
        if psum==target:
            self.a_hash.add(tuple(arr))
            return
            # self.res.append(arr)
        for ind in range(index, len(self.cands)):
            j = ind+0
            while(ind<(len(self.cands)-1) and self.cands[ind]==self.cands[ind+1]):
                ind+=1
            self.comb(target,arr+[self.cands[j]],psum+self.cands[ind],j+1)



sol =  Solution()

arr =[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] 
target = 27

print(sol.combinationSum2(arr, target))