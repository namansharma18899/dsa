class Solution:
    def kidsWithCandies(self, candies, extraCandies: int):
        greatest = max(candies)
        return [True if candy+extraCandies>=greatest else False for candy in candies ]
    


sol = Solution()
candies = [4,2,1,1,2]
extra = 1

print(sol.kidsWithCandies(candies, extra))