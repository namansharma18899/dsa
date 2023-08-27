from typing import List
class Solution:
    """
    TLE: not memory efficient
    """
    def longestOnes(self, nums: List[int], k: int) -> int:
        return self.getRes(nums, k, 0)
    
    def getRes(self, nums, k, index):
        curr = self.calculate(nums)
        if k<=0 or index>=len(nums):
            return curr
        if nums[index] == 0:
            num2 = [] + nums
            num2[index]=1
            res1 = self.getRes(num2, k-1, index+1)
            res2 = self.getRes(nums, k, index+1)
            return max(max(res1, res2), curr)
        else:
            res2 = self.getRes(nums, k, index+1)
            return max(res2, curr)

    def calculate(self, nums):
        n2 = []+nums
        for index in range(1, len(n2)):
                if n2[index]==0:
                    continue
                else:
                    n2[index]+=n2[index-1]
        return max(n2)



sol = Solution()

nums =[0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3

print(sol.longestOnes(nums, k))

