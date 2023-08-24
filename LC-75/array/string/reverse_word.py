def char_is_space(arr ,index):
    if(index<0 or index>=len(arr)):
        return False
    else:
        return True if arr[index]==' ' else False
class Solution:
    """
    my sol:
    time complexity: O(N)
    space complexity: O(N)
    """
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        res = list(s)
        res2 = list()
        p1 = 0
        """
        cleanup spaces in b/w
        """
        for index in range(0, len(res)):
            if res[index]==' ':
                if (not char_is_space(res, index-1)):
                    res2.append(' ')
            else:
                res2.append(res[index])
        p1 = 0
        p2 = len(res2)-1
        result = ""
        while(p1 < p2):
            temp = res2[p1]
            res2[p1] = res2[p2]
            res2[p2] = temp
            p1+=1
            p2-=1
        p1 = 0
        for index in range(0, len(res2)):
            if(res2[index]==' '):
                result+=(''.join(res2[p1:index][::-1]))
                p1 = index+1
                result+=' '
        result+=(''.join(res2[p1:index+1][::-1]))
        # reverse the string in the same order
        return result



sol = Solution()
s = "  the sky    is blue  "

print(sol.reverseWords(s))