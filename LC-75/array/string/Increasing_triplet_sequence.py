from Leetcode.utils.utility import timer

# class Solution:
#     @timer
#     def increasingTriplet(self, num):
#         """
#         brute force: 
#         O(N3)
        # """
        # for index in range(0, len(num)):
        #     for j in range(index+1, len(num)):
        #         if num[j] > num[index]:
        #             for k in range(j+1, len(num)):
        #                 if num[k] > num[j]:
        #                     return True
        # return False
class Solution:
    def increasingTriplet(self, nums) -> bool:
        first = second = float('inf') 
        for n in nums: 
            if n <= first: 
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False



sol = Solution()
arr = [9,8,7,6,5]
print(sol.increasingTriplet(arr))