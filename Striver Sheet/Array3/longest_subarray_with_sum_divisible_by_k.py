arr = [2, 7, 6, 1, 4, 5]
k = 3
result = 0

class Res:
    result = 0
    def fun(self, arr, sum,start, posi, k):
        if posi>=len(arr):
            return sum
        # start from here, skip this, add this
        if sum%k==0:
            self.result = max(self.result, posi-start)
        a_from_here  = self.fun(arr, arr[posi],posi,posi+1,k)
        include_here = self.fun(arr, sum+arr[posi],start,posi+1,k)


obj = Res()
obj.fun(arr,0,0,0,3)
print('res -> ', obj.result)