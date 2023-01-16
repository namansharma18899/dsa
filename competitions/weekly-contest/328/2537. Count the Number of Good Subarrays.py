# from utils import *
from collections import Counter


class Solution:
    def countGood(self, nums, k: int) -> int:
        return self.recur(nums, 0, k, [])

    def recur(self, nums, i, k: int, temp=[]):
        pass


def fun(args):
    sol = Solution()
    return sol.countGood([int(x) for x in args], int(input()))


if __name__ == '__main__':
    print(fun(input().split(',')))
