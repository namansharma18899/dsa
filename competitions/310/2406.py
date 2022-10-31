import heapq

class Obj:
    def __init__(self,l,r):
        self.l, self.r = l,r
# 1. greedy
def fun():
    intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
    h = []
    print(sorted(intervals, key = lambda x: x[0]))
    import pdb; pdb.set_trace()
    for s,e in sorted(intervals,key = lambda x:x[0]):
        print(e)
        if not h:
            heapq.heappush(h,e)
        else:
            mn = heapq.heappop(h)
            if s <= mn:
                heapq.heappush(h,mn)
            heapq.heappush(h,e)
    print(h)
    return len(h)


print(fun())