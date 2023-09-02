from collections import Counter, defaultdict


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """
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
        """
        c1 = Counter(word1)                                         #          c1 = {'a':2, 'b':3, 'c':1}
        c2 = Counter(word2)                                         #          c1 = {'a':2, 'b':3, 'c':1}

        count1 = sorted(c1.values())                                #      count1 = [1, 2, 3]
        count2 = sorted(c2.values())                                #      count2 = [1, 2, 3]

        set1 = set(word1)                                           #        set1 = {'c', 'b', 'a'}
        set2 = set(word2)                                           #        set2 = {'a', 'c', 'b'}

        if count1 == count2 and set1 == set2:                       #      return True
            return True

        return False