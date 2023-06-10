#from utils import *
class Solution:
    def traverse(self, m,n,i,j):
        #boundary conditions
        if i>=m or j>=n:
            return 0
        if i==(m-1):
            return 1
        if j==(n-1):
            return 1
        #other cases
        return  self.traverse(m,n,i+1,j)+self.traverse(m,n,i,j+1)

    def uniquePaths(self, m: int, n: int) -> int:
        "no intuition just struck, going with the flow for now"
        return self.traverse(m,n,0,0)
        

def fun(args=None):
    sol = Solution()
    return sol.uniquePaths(int(input()),int(input()),)


if __name__=='__main__':
    print(fun())#input().split(',')))