from collections import Counter
from typing import List


class Solution:

    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate = nums[0]
        count = 1
        max =1
        mxc = 0
        for index in range(1, len(nums)):
            if nums[index]!=candidate:
                count-=1
            elif nums[index]==candidate:
                count+=1
            if count==0:
                candidate=nums[index]
                count=1
        res = []
        if count>(len(nums)/3):
            res.append(candidate)
        candidate2 = nums[0]
        count = 1
        max =1
        mxc = 0
        for index in range(1, len(nums)):
            if nums[index]==candidate:
                count-=1
                continue
            if nums[index]!=candidate2:
                count-=1
            elif nums[index]==candidate2:
                count+=1
            if count==0:
                candidate2=nums[index]
                count=1
        if count>(len(nums)/3):
            res.append(candidate2)
        return res

def fun():
    sol = Solution()
    el = input().split(',')
    args = [int(x) for x in el]
    return sol.majorityElement(args)


if __name__ == '__main__':
    tcs = int(input())
    while tcs > 0:
        print('res -> ', fun())
        tcs -= 1
