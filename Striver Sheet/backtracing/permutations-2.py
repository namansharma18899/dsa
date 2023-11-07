class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = set()
        def swap(p1, p2):
            temp = nums[p1]
            nums[p1] = nums[p2]
            nums[p2] = temp
            
        def perm_helper(index):
            if index==len(nums)-1:# we reached bounday
                result.add(tuple(nums))
                return
            for ind in range(index+1, len(nums)):
                swap(ind, index)
                perm_helper(ind) 
                swap(index,ind) # swap back the values
                
        for ind in range(0, len(nums)):
            perm_helper(ind) 
        return list(result)
