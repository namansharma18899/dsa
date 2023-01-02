class Solution:
    def countDigits(self, num: int) -> int:
        n= num
        count =0
        while(n>0):
            div = int(n%10)
            if num%div==0:
                count+=1
            n=int(n/10)
        return count
            