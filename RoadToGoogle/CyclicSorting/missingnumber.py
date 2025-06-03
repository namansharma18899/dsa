class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        for i in range(0, len(nums)+1):
            sum+=i
        sm = 0 
        for val in nums:
            sm+=val
        return sum - sm


obj = Solution()

arrs = [
[0,1,2,4,5,6,7], 
[0,1,2,4,5,6,7,8], 
[1,2],
[1]
]
for arr in arrs:
    print('res -> ', obj.missingNumber(arr))