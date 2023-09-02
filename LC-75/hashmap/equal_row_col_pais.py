from collections import Counter, defaultdict
from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        pairs = 0
        counters = []
        count = 0
        for row in grid:
            for col in grid:
                c = Counter(col)
                if c in counters:
                    count+=1
                else:
                    counters.append(c)
                    count-=1
        """
        tbc
        """