class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count=0
        for each in zip(*strs):
            if list(each)!=sorted(each):
                count+=1
        return count