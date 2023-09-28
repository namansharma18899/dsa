#User function Template for python3
from Leetcode.utils.utility import timer


class Train:
    def __init__(self, arr, dep):
        self.arr = int(arr)
        self.dep = int(dep)


class Solution:
    """Function to find the minimum number of platforms required \
    at the railway station such that no train waits.
    """
    @timer
    def minimumPlatform(self, arr, dep):
        n = len(arr)
        objs = list()
        for index in range(0, n):
            objs.append(Train(str(arr[index]), str(dep[index])))
        objs.sort(key=lambda x: x.arr)
        queue = [objs.pop(0).dep]
        index = 0
        for train in objs:
            found = False
            ln = len(queue)
            index = ln-1 if ln > 0 else 0
            while (index >= 0):
                if train.arr >= queue[index]:
                    found = True
                    queue[index] = train.dep
                    break
                index = index - 1
            if not found:
                queue.append(train.dep)
        return len(queue)


def fun():
    sol = Solution()
    arr = [int(x) for x in input().split(' ')]
    dep = [int(x) for x in input().split(' ')]
    return sol.minimumPlatform(arr, dep)


if __name__ == "__main__":
    tcs = int(input())
    while (tcs > 0):
        print('res -> ', fun())
        tcs -= 1
