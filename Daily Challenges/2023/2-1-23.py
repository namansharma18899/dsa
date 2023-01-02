#from utils import *
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper() or word.islower():
            return True
        if word[0].isupper() and word[1:].islower():
            return True
        return False

def fun(args):
    sol = Solution()
    return sol.detectCapitalUse(args)


if __name__=='__main__':
    print(fun(input()))