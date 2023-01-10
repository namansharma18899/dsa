# from Leetcode.utils.utility import swap



class Solution:
    nums = 0
    def swap(self,arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    def nextPermutation(self, nums):# List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #1 3 2 4  1 3 4 2  1 4 3 2 ..... 3 2 1  1 2 4 3
        self.nums = nums
        for index in range(len(nums)-1,0,-1):
            if nums[index]>nums[index-1]:
                #find next greatest element wrt this number
                res = index
                for j in range(index+1, len(nums)):
                    if nums[j]>nums[index-1]:
                        res=j
                self.swap(nums,index-1,res)
                #now we have 5, 1, 4, 3, 2 -> 5, 2, 4, 3, 1
                nums[index:]=nums[index:][::-1]
                return 
        nums[0:len(nums)]= nums[::-1]
        self.nums=nums




def fun(args):
    sol = Solution()
    sol.nextPermutation([int(x) for x in args])
    return sol.nums
    # return sol.nextPermutation([int(x) for x in args])


if __name__=='__main__':
    print(fun(input().split(',')))