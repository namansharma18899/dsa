from collections import defaultdict


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        f1 = defaultdict(int)
        f2 = defaultdict(int)
        if len(word1)!=len(word2):
            return False        
        for each in word1:
            f1[each]+=1
        for each in word2:
            f2[each]+=1
        if len(f1) != len(f2):
            return False
        c1 = set(k for k in f1.keys())
        c2 = set(k for k in f2.keys())
        if c1!=c2:
            return False
        v1 = [v for k,v in f1.items()]
        v2 = [v for k,v in f2.items()]
        v1.sort()
        v2.sort()
        if v1!=v2:
            return False
        return True