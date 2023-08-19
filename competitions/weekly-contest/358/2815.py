#from utils import *
from collections import Counter, defaultdict
import heapq
""""
My try
Status -> Failed in a testcase
"""
class MaxHeapWithTwoElements:
    def __init__(self):
        self.heap = []

    def push(self, val):
        if len(self.heap) < 2:            
            heapq.heappush(self.heap, -val)  # Store negative values to simulate max heap behavior
        else:
            if val > -self.heap[0]:
                temp = -self.heap[0]
                heapq.heappop(self.heap)
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, -temp) #max
                heapq.heappush(self.heap, -val)# new replaced
            elif val > -self.heap[1]:
                temp = -self.heap[0]
                heapq.heappop(self.heap)
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, -temp) #max
                heapq.heappush(self.heap, -val)# new replaced

    def get_max(self):
        if self.heap:
            return -self.heap[0]
        return 0

    def get_second_max(self):
        if len(self.heap) > 1:
            return -self.heap[1]
        return 0


def max_digit(number):
    max_digit = -1  # Initialize with a value lower than any digit
    while number > 0:
        digit = number % 10
        max_digit = max(max_digit, digit)
        number //= 10
    return max_digit

def digit_frequency(number, digit):
    freq =  str(number).count(str(digit))
    if freq==len(str(number)):
        return 1
    else:
        return freq

# Example usage
if __name__=="__main__":
    heaps = {}
    # arr = [84,91,18,59,27,9,81,33,17,58]
    # arr = [35,52,74,92,25,65,77,1,73,32]
    # arr = [68,8,100,84,80,14,88]
    arr = [5,1506,1778,1943,707,1619,2383,35,1315,1188,2455,1396,596,2440,1706,324,1569,905,418,1065,76,2421,1701,1885,1916]
    # for each in arr:
    #     max_d = max_digit(each)
    #     freq = digit_frequency(each, max_d)
    #     if(f'{max_d}-{freq}' not in heaps.keys()):
    #         heaps[f'{max_d}-{freq}'] = MaxHeapWithTwoElements()
    #     heaps[f'{max_d}-{freq}'].push(each)

    # result = -99
    # for key, hp in heaps.items():
    #     if(hp.get_max()+hp.get_second_max() > result):
    #         result = hp.get_max()+hp.get_second_max()

    # print(result)

    """
    Solution
    """
    res = -1
    # nums = [68,8,100,84,80,14,88]
    nums = [5,1506,1778,1943,707,1619,2383,35,1315,1188,2455,1396,596,2440,1706,324,1569,905,418,1065,76,2421,1701,1885,1916]
    max_nums = defaultdict(int)
    for each in nums:
        max_digit = max(str(each))
        if max_digit in max_nums.keys():
            # maximum pair sum at this point of time
            res = max(res, each+max_nums[max_digit])
        max_nums[max_digit] = max(each, max_nums[max_digit])
    print(res)

    """
    PROBLEM : Did not understand the problem statement properly
    """