from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """
        left highest and right highes
        """
        i = 0
        prevZ = None
        psum =0
        res = 0
        while(i < len(nums)):            
            if nums[i]==0:
                if not prevZ:
                    prevZ = i
                else:
                    psum = i - prevZ -1
                    prevZ = i
            else:
                psum+=1
            res = max(res, psum)
            i+=1
        return res if prevZ is not None else res-1