class Solution:
    def fun(self,nums):
        nums = [int(x) for x in nums]
        k = int(input())
        #nums =[1,2,3,4,5,6] k = 2
        #an = [5,6,1,2,3,4]
        n = len(nums)
        if k>n:
            n=int(k/(n-1))
        self.reverse(nums,n-k,n-1)
        self.reverse(nums,0,n-k-1)
        self.reverse(nums,0,n-1)
        return nums
    def swap(self,nums, i, j):
        temp = nums[i]
        nums[i]=nums[j]
        nums[j]=temp

    def reverse(self,nums, first, last):
        index = first
        while(first<last):
            self.swap(nums,first,last)
            first+=1
            last-=1
        

if __name__=='__main__':
    x = Solution()
    print(x.fun(input().split(',')))
    # print(fun(input().split(',')))