from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        candidates.sort()
        print(len(candidates))
        temp = []

        def helper(target, ind):
            if target==0:
                res.add(tuple(temp))
                return
            if target < 0 or ind>=len(candidates):
                print('in re')
                return
            temp.append(candidates[ind])it
            helper(target-candidates[ind], ind+1)
            temp.pop()
            temp_ind = ind+0
            # we want to skip all the same nums cause they will result in the same trees which we just computed.
            while(temp_ind<len(candidates)-1 and candidates[temp_ind]==candidates[temp_ind+1]):
                temp_ind+=1
            print('tic -> ', temp_ind)
            temp.append(candidates[temp_ind])
            helper(target-candidates[temp_ind], ind+1)
            temp.pop()
        
        helper(target, 0)
        return list(res)


sol =  Solution()

arr =[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] 
target = 27

print(sol.combinationSum2(arr, target))