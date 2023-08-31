class Solution:
    def longestOnes(self, nums, k: int) -> int:
        j = 0
        i = 0
        mx= -99
        while(j< len(nums)):
            if nums[j]==0:
                k-=1
            while(k<0):
                if nums[i]==0:
                    k+=1
                i+=1
            mx = max(mx, (j-i+1))
            j+=1
        return mx



sol = Solution()

nums =[0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3

print(sol.longestOnes(nums, k))