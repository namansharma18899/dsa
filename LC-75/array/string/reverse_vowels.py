class Solution:
    def reverseVowels(self, s: str) -> str:
        i = 0
        j = len(s)-1
        res = list(s)
        while( i <= j ):
            if s[i] in ['a','e','i','o','u','A','E','I','O','U'] and s[j] in ['a','e','i','o','u','A','E','I','O','U']:
                res[j] = s[i]
                res[i] = s[j]
                i+=1
                j-=1
            else:
                if s[i] not in ['a','e','i','o','u','A','E','I','O','U']: 
                    i+=1
                if s[j] not in ['a','e','i','o','u','A','E','I','O','U']: 
                    j-=1
        return ''.join(res)