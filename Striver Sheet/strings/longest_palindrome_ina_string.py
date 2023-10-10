class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        def is_palin(l, r):
            while(l>=0 and r<=len(s)-1) and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1:r]
                
        res = "" 
        for index in range(len(s)):
            res = max(res, is_palin(index, index), is_palin(index,index+1),key= lambda x: len(x))
        return res

st = 'abb'

print(Solution().longestPalindrome(st))