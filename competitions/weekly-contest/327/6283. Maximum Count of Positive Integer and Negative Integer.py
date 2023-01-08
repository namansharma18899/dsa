#from utils import *

class Solution:
    def maximumCount(self, nums) -> int:
        mp = 0
        print(nums)
        mn=0
        for each in nums:
            if each>0:
                mp+=1
            elif each<0:
                mn+=1
        return max(mn,mp)

def fun(args):
    sol = Solution()
    return sol.maximumCount([int(x) for x in args])


if __name__=='__main__':
    print(fun(input().split(',')))