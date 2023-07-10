#from utils import *

"""
intutin -> removing the dupolicats 

prblm -> sets were unhashable plus couldn't hash duplicates prpoley 
created tuple of sorted(array)
"""


class Solution:
    def subsetsWithDup(self, nums):
       val = self.generateSset(nums, 0, [])
       return val
    def generateSset(self, nums, index, sset):
        if index>=len(nums):
            return [sset]
        #Cannot hash lists -> not a good choice...
        val1 = self.generateSset(nums, index+1,sset)
        sset2= []+sset
        sset2.append(nums[index])
        val2 = self.generateSset(nums, index+1,sset2)
        los_set_1 = [tuple(sorted(_el)) for _el in val1]
        los_set_2 = [tuple(sorted(_el)) for _el in val2]
        res = los_set_1
        for each in los_set_2:
            if each not in res:
                res.append(each)
        return [list(_) for _ in res]


def fun(args):
    sol = Solution()
    print(sol.subsetsWithDup([1,2,2]))


if __name__=='__main__':
    fun(args={})