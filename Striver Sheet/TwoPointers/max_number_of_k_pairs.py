deletion = set()
def mark_for_deletion(i, j):
    deletion.add(i)
    deletion.add(j)

class Solution:
    def maxOperations(self, nums, k: int) -> int:
        nums = sorted(nums)
        second = 1
        """
        brute force
        """
        for index in range(0, len(nums)-1):
            for second in range(index+1, len(nums)):
                if(second in deletion):
                    continue
                if(nums[index]+nums[second] < k):
                    second+=1
                elif(nums[index] + nums[second] == k):
                    mark_for_deletion(index, second)
                else:
                    second = index+1
        return int(len(deletion)/2)

sol = Solution()
nums = [3,1,3,4,3]
k = 6
print(sol.maxOperations(nums, k))



"""
1. brute force -> 

"""