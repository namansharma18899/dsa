from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        self.mem = [0 for _ in range(len(nums))]
        def calc_lis(nums,ind, prev_ind):
            def is_curr_part_of_lis(nums,ind, prev_ind) -> bool: 
                return nums[ind]>nums[prev_ind]
            if ind>=len(nums):
                return 0
            chosen_curr = 0
            skipped_curr = 0
            if ind==prev_ind or is_curr_part_of_lis(nums,ind, prev_ind):
                if self.mem[ind]==0:
                    self.mem[ind] = 1 + calc_lis(nums, ind+1, ind+0)
                chosen_curr = self.mem[ind]
            skipped_curr = calc_lis(nums, ind+1, prev_ind)
            return max(skipped_curr, chosen_curr)
        for each in range(0, len(nums)):
            calc_lis(nums, each, each+0)
        print(self.mem)
        return max(max(self.mem),1)


from typing import List

def fun(args):
    sol= Solution()
    return sol.lengthOfLIS(args)


if __name__=='__main__':
    # tcs = int(input())
    tcs=[
        [10, 9, 2, 5, 3, 7, 101, 18],
        [0,1,0,3,2,3],
        [1,1,1,1,1,1]
    ]
    for each in tcs:
        print('testcase -> \n')
        print(fun(each))
    # while(tcs>0):
    #     print('res -> ',fun())
    #     tcs-=1
