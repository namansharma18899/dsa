class Solution:
    def maxOperations(self, nums, k: int) -> int:
        nums = sorted(nums)
        second = 1
        """
        brute force
        """
        # for index in range(0, len(nums)-1):
        #     for second in range(index+1, len(nums)):
        #         if(second in deletion):
        #             continue
        #         if(nums[index]+nums[second] < k):
        #             second+=1
        #         elif(nums[index] + nums[second] == k):
        #             mark_for_deletion(index, second)

        """
        time-> o(n log(n))
        space -> O(n)
        """
        # mxNum = max(nums)
        # deletion = [0 for _ in range(0, max(mxNum+1, k))]
        # pairs = 0
        # for each in nums:
        #     if each > k:
        #         break
        #     if deletion[each] >= 1:
        #         pairs+=1
        #         deletion[each]-=1
        #     else:
        #         deletion[k-each]+=1        
        # return pairs
        """
        time -> O( n logn )
        space -> O(1)
        """
        i=0
        j= len(nums)-1
        count = 0
        while(i<j):
            if(nums[i]+nums[j]==k):
                count+=1
                i+=1
                j-=1
            elif(nums[i]+nums[j]<k):
                i+=1
            else:
                j-=1
        return count


    
sol = Solution()
nums = [1,2,3,4]
k = 5
print(sol.maxOperations(nums, k))



"""
1. brute force -> 

"""