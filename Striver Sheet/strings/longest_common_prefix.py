from typing import List

"""
Better approach Tries
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prev = strs.pop(0)
        for each in strs:
            ind = 0
            temp = ""
            while(ind < len(min(each, prev))):
                if prev[ind]==each[ind]: temp+=prev[ind]
                else: break
                ind+=1
            prev = temp
        return prev