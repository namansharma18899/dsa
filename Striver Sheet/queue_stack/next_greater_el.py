from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]):
        result = []
        for n_i in nums1:
            n_i_index_in_nums2 = nums2.index(n_i)
            arr: list = []
            for i_j in range(len(nums2)-1, n_i_index_in_nums2-1,  -1):
                el = nums2[i_j]
                while(len(arr)>0 and el > arr[-1]):
                    arr.pop()
                if el == n_i:
                    result.append(arr[-1] if len(arr)>0 else -1)
                else:
                    arr.append(el)
        return result


sol = Solution()
print(sol.nextGreaterElement([2,4], [1,2,3,4]))