class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set([])
        def subsetHelper(temp, ind):
            if ind>=len(nums):
                temp.sort()
                res.add(tuple(temp))
                return
            temp.append(nums[ind])
            subsetHelper(temp, ind+1)
            temp.pop()
            subsetHelper(temp, ind+1)
        subsetHelper([],0)
        return list(res)
