#from utils import *
class Solution:
    def answerQueries(self, nums, queries):
        self.min = 999
        nums = sorted(nums)
        res =[]
        psum = [nums[0]]
        for index in range(1, len(nums)):
            psum.append(psum[index-1]+nums[index])
        for index, each in enumerate(queries):
            temp = None
            for ind, val in enumerate(psum):
                if val<=each:
                    temp=ind
                else:
                    break
            res.append(temp+1 if temp is not None else 0)
        #     loc = self.bin_search(nums, 0,len(nums), queries[index])
        #     res[index] = self.loc+1 if loc==-1 else loc+1
        return res

    def bin_search(self, arr, low, high, x):
        # Check base case
        if high >= low:
            mid = (high + low) // 2
            # If element is present at the middle itself
            if arr[mid] == x:
                return mid
            if int(x-mid) > 0 and int(x-mid) < self.min:
                self.min = int(x-mid)
                self.loc = mid
            elif arr[mid] > x:
                return self.binary_search(arr, low, mid - 1, x)
            # Else the element can only be present in right subarray
            else:
                return self.binary_search(arr, mid + 1, high, x)
        else:
            # Element is not present in the array
            return -1

def fun(args):
    sol = Solution()
    y = [int(y) for y in  input().split(',')]
    z = [int(x) for x in args]
    return sol.answerQueries(z,y)


if __name__=='__main__':
    print(fun(input().split(',')))