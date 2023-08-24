class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if(len(str2) > len(str1)):
            temp = str1
            str1 = str2
            str2 = temp
        result = ""
        for index in range(1, len(str2)+1):
            el = str2[:index]
            if(int(len(str1) % len(el))==0 and  (el* int(len(str1)/len(el))) == str1): # it divides the string
                if(int(len(str2) % len(el))==0 and  (el* int(len(str2)/len(el))) == str2):
                    result = el
        return result
    


sol = Solution()
s1 = "asdf"
s2 = "bb"

print(sol.gcdOfStrings(s1, s2))