#from utils import *
from collections import Counter


class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        k1 = Counter(word1)
        k2 = Counter(word2)
        s1 = set(k1.keys())
        s2 = set(k2.keys())
        low = k1
        high= k2
        inst = s1.intersection(s2)
        if len(s1)>len(s2):
            return self.check(k2,k1,inst)
        else:
            return self.check(k1,k2,inst,word1,word2)

    def check(self, low,high,inst,word1,word2):
        pass
        # if len(set(high)) - len(set(low)) >2:
        #         return False
        # elif len(inst)==0:
        #     if len(word1)==len(word2):
        #         return True
        #     return False
        # else:
        #     #now check swappable entitity in low
        #     # get intersection item with max vals in high
        #     found_low_swappable = False
        #     for k,v in low.items():
        #         if k in inst and v>1:
        #             found_low_swappable=True
        #             break
        #     if not found_low_swappable: return False
        #     for k,v in high.items():
        #         if k not in inst and v>1:
        #             return True 
        

def fun(args):
    sol = Solution()
    return sol.isItPossible(args[0], args[1])


if __name__=='__main__':
    print(fun(input().split(',')))