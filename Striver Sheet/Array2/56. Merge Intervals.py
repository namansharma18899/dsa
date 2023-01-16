#from utils import *
import numpy as np

class Solution:
    def merge(self, arr):
        arr = arr[arr[:, 0].argsort()]
        print(arr)
        result = [arr[0]]
        for index in range(1,len(arr)):
            if arr[index][0]<=result[-1][1]:
                result[-1][1]=max(arr[index][1],result[-1][1])
            else:
                result.append(arr[index])
        return result
        

def fun():
    sol = Solution()
    args = np.array(tuple([[1,4],[2,3]]))
    return sol.merge(args)


if __name__=='__main__':
    print(fun())




#Initial Intuition->