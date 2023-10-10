class Solution:
    def romanToInt(self, s: str) -> int:
        hmap = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        num = 0
        index= 0
        while(index < len(s)):
            sm = hmap[s[index]]
            if index+1 < len(s) and  hmap[s[index+1]] > sm:
                num+= hmap[s[index+1]] - sm
                index+=2
                continue
            else:
                num+=sm
            index+=1
        return num
