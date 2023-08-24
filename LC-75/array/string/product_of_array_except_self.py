class Solution:
    def productExceptSelf(self, nums):
        product = None
        zeroCount = 0
        for each in nums:
            if each!=0:
                product = 1 if product is None else product
                product*=each
            else:
                zeroCount+=1
        product = 0 if (product is None) else product
        if zeroCount==1:
            return [int(product) if each==0 else 0 for each in nums]
        elif zeroCount>1:
            return [0 for each in nums]
        else:
            return [int(product/each)  for each in nums]


sol = Solution()
nums = [-1,1,0,-3,3]

print(sol.productExceptSelf(nums))