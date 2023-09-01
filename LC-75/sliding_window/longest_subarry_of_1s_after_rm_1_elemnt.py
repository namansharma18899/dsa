from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """
        left highest and right highes
        """
        res = 0
        index = 0
        start= 0
        zcount = 0
        while(index < len(nums)):
            if nums[index]==0:
                zcount+=1
            while(zcount> 1):
                if nums[start]==0:
                    zcount-=1
                start+=1
            res= max(res, index-start)
            index+=1
        return res 