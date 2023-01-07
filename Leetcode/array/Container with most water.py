class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_volume = -99
        l=0
        r=len(height)-1
        while(l<r):
            max_volume = max((min(height[l],height[r]) * int(r-l)), max_volume)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max_volume