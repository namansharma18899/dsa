#from utils import *
class Solution:
    def maximumBags(self, capacity, rocks, additionalRocks: int) -> int:
        #initial fill
        for index, val in enumerate(rocks):            
            capacity[index]-=val
        #to fillleast capacity to most
        result = 0
        capacity=sorted(capacity)
        for index in range(0, len(capacity)):
            if capacity[index]>additionalRocks:
                return result
            else:
                additionalRocks-=capacity[index]
                result+=1
        return result


def fun(args):
    sol = Solution()
    addition_rocks= int(input())
    return sol.maximumBags(args, [int(rock) for rock in input().split(',') ], addition_rocks)
    return args


if __name__=='__main__':
    print(fun([int(rock) for rock in input().split(',')]))