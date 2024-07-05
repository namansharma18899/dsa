from typing import List


class Solution:
    result = 0
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        self.covered_subarrays:list = []
        self.fun(nums, 0, 0, 0, k)
        return self.result

    def fun(self, arr, sm,start, posi, k):
        if posi>=len(arr):
            return None
        
        # if (start,posi) not in self.covered_subarrays:
        #     sm+=arr[posi]
        #     if abs(sm)%k==0:
        #         self.covered_subarrays.append((start,posi))
        #         print('res sum -> ', sm, '  pos -> ', start, posi)
        #         self.result+=1
        # if (posi,posi) not in self.covered_subarrays:
        #     if abs(arr[posi])%k==0:
        #         self.covered_subarrays.append((posi,posi))
        #         print('res -> ', arr[posi])
        #         self.result+=1
        # self.fun(arr, arr[posi],posi,posi+1,k)
        # self.fun(arr, sm, start, posi+1,k)



sol = Solution()
print(sol.subarraysDivByK(nums=[2,-2,2,-4],k=6))
    # ums=[2,-2,2,-4]),k=6)