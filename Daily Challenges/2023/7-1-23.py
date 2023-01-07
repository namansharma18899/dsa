#from utils import *
class Solution:
    def twoSum(self, numbers, target: int):# -> List[int]:
        l = 0
        r = len(numbers)-1
        while(l<r):
            if numbers[l]+numbers[r]==target:
                return [l+1,r+1]
            elif numbers[l]+numbers[r]>target:
                r-=1
            else:
                l+=1
        return -1

def fun(args):
    sol = Solution()
    return sol.twoSum([int(x) for x in args],int(input()))


if __name__=='__main__':
    print(fun(input().split(',')))