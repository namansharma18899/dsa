#from utils import *

from collections import Counter

class Solution:
    def maxSum(self) -> int:
        args = [1,2,3,4]
        """
        brute force: O ( n * n )
        """
        result = None
        for index in range(0,len(args)):
            for i_j in range(index+1, len(args)):
                """
                calculate same freq. sum 
                """
                sum_i_j = args[index] + args[i_j]
                if (sum_i_j%10) == (int(sum_i_j / 10)):
                    result = sum_i_j if ((result is None ) or sum_i_j > result) else result
        return -1 if result is None else result


def fun():
    sol = Solution()
    return sol.maxSum()


if __name__=='__main__':
    print(fun())