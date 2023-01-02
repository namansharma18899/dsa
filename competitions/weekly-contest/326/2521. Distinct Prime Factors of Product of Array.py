
class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        prod=1
        for each in nums:
            prod*=each
        return len(self.get_primes(prod))
    
    def get_primes(self,n):
        c = 2
        yielded = set()
        while(n > 1):
            if(n % c == 0):
                yielded.add(c)
                n=n//c
            else:
                c = c + 1
            print(n, ' ',c)
        print(yielded)
        return yielded