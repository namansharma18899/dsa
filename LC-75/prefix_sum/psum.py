from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        mx = 0
        prev = 0
        for each in gain:
            prev = each + prev
            mx = max(mx, prev)
        return mx