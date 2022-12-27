from collections import defaultdict
class Obj:
    def __init__(self,count, num):
        self.count =count
        self.num=num
class Solution:
    def topKFrequent(self, nums,k):# List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        for each in nums:
            frequency[each]+=1
        objs = []
        for key,v in frequency.items():
            objs.append(Obj(v,key))
        objs.sort(key=lambda x: x.count, reverse=True)
        return [obj.num for obj in objs[:k]]

def fun(arr):
    sol = Solution()
    return sol.topKFrequent([1,1,1,1,1,2,2,4,4,4],2)


if __name__=='__main__':
    tcs = int(input())
    while(tcs>0):
        print('res -> ',fun(input().split(',')))
        tcs-=1