class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurances = defaultdict(int)
        for each in arr:
            occurances[each]+=1
        return True if len(set([v for k,v in occurances.items()])) == len(occurances) else False
