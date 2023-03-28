# User function Template for python3
import xml.dom.domreg


class Item:
    def __init__(self, val, w):
        self.value = val
        self.weight = w


class Solution:
    def fractionalknapsack(self, W, arr, n):
        arr = sorted(arr, key=lambda x: x.value / x.weight)
        result = 0
        while W > 0 and len(arr) > 0:
            # w = 20, value/wration = x ther. sum=x*
            x = arr.pop()
            value_weight_ratio = x.value / x.weight
            result += int(min(W, x.weight)) * value_weight_ratio
            W -= min(W, x.weight)
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
