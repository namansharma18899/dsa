class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if(len(s) > len(t)):
            return False
        if(s==""):
            return True
        p1 = 0
        p2 = 0
        while(p1 < len(s) and p2 < len(t)):
            each = t[p2]
            if each==s[p1]:
                p1+=1
            if(p1==len(s)):
                return True
            p2+=1
        return False
