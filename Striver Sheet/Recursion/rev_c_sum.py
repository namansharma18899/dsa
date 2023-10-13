from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # self.cands = list(set(candidates))
        self.cands = sorted(candidates)
        self.a_hash = set()
        self.res =[] 
        self.comb(target, [], 0, 0)
        return self.res

    def comb(self, target,arr, psum, index):
        if psum>target:
            return
        if psum==target:
            self.res.append(arr)
        for ind in range(index, len(self.cands)): 
            if psum+self.cands[ind] > target:
                return
            self.comb(target,arr+[self.cands[ind]],psum+self.cands[ind],ind)
        # if index >= len(self.cands):
        #     return []
        # if psum==target:
        #     if tuple(arr) in self.a_hash:
        #         return []
        #     else:
        #         self.a_hash.add(tuple(arr))
        #         return [arr]
        # elif psum> target:
        #     return []
        # # choose me
        # res = []
        # trr = arr + [self.cands[index]]
        # res+=self.comb(target, trr, psum+self.cands[index], index+1)
        # res+=self.comb(target, arr, psum,index+1)
        # return res

    

sol = Solution()

arr = [2,5,2,1,2]
psum = 8

print(sol.combinationSum2(arr, psum))