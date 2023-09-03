class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows_counts = Counter(map(tuple, grid))
        columns = zip(*grid)
        res = 0
        for each in columns:
            if each in rows_counts:
                res+=rows_counts[each]
        return res