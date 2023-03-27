# User function Template for python3

class Item:
    def __init__(self, val, w):
        self.value = val
        self.weight = w


class Solution:
    def fractionalknapsack(self, W, arr, n):
        sorted(arr, key=lambda x: int(x.weight / x.value))
        result = 0
        index = 0

        return result


def fun():
    x = Solution()
    weight = int(input())
    wgts = [int(x) for x in input().split(',')]
    vals = [int(x) for x in input().split(',')]
    items = list()
    for index in range(0, len(wgts)):
        items.append(Item(vals[index], wgts[index]))
    return x.fractionalknapsack(weight, items, len(wgts))


if __name__ == '__main__':
    tcs = int(input())
    while (tcs > 0):
        print('res -> ', fun())  # input().split(',')))
        tcs -= 1
