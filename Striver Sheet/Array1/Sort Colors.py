#from utils import *
class Solution:
    def swap(self,arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def sortColors(self, nums):#List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # I can sort all 0's then all 1's
        prev_zero_index = 0
        prev_one_index = 0
        for index in range(0,len(nums)):
            if nums[index]==0:
                self.swap(nums,index,prev_zero_index)
                prev_zero_index+=1
        # for index in range(prev_index,len(nums)):
            elif nums[index]==1:
                self.swap(nums,index,prev_one_index)
                prev_one_index+=1
        return nums
        

def fun(args):
    sol = Solution()
    return sol.sortColors([int(x) for x in args])


if __name__=='__main__':
    print(fun(input().split(',')))