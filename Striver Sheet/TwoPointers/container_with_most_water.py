class Solution:
    def maxArea(self, height) -> int:
        if(len(height))==2:
            return min(height[0], height[1])
        p1, p2 = 0, len(height)-1
        maxvol = 1 # edge case of two towers
        while(p1<p2):
            volume = ((p2 - p1)) * (min(height[p2], height[p1]))
            maxvol = max(volume, maxvol)
            if(height[p2]<height[p1]):
                p2-=1
            else:
                p1+=1
        return maxvol


sol = Solution()
heights = [3,2]
print(sol.maxArea(heights))