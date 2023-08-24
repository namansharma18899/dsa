class Solution:
    def check(self, arr, index):
        if(index<0) or index>=len(arr):
            return True
        else:
            return True if arr[index]==0 else False
        
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        #handle 1 flower case
        if n==0:
            return True
        if(len(flowerbed)==1):
            return True if flowerbed[0]==0 and n==1 else False
        for index in range(0, len(flowerbed)):
            if(self.check(flowerbed, index) and self.check(flowerbed, index-1) and self.check(flowerbed, index+1)):
                flowerbed[index]=1
                n-=1
        return True if n<=0 else False

sol = Solution()
arr= [1,0,0,0,0,1]
n = 2
print(sol.canPlaceFlowers(arr, n))