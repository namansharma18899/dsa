from collections import Counter, defaultdict
from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        counter = [0]*(len(grid)*len(grid[0]))#mxn
        freq = []
        res  = 0
        for row in grid:
            freq.append(row)
        freq2 = []
        for i in range(len(grid[0])):
            col = []
            for j in range(len(grid)):
                col.append(grid[j][i])
            freq2.append(col)
        for each in freq:
            for j in freq2:
                if each == j:
                    res+=1
        return res
    

obj = Solution()
grid = [[3,2,1],[1,7,6],[2,7,7]]
print(obj.equalPairs(grid))