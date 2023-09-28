# from utils import *
class Solution:
    def traverse(self,i,j):
        if i==0 and j==0: return 1 
        if self.temp[i][j]!=-1:
            return self.temp[i][j]
        cnt = 0
        if i>0:
            cnt+=self.traverse(i-1,j)
        if j>0:
            cnt+=self.traverse(i,j-1)
        self.temp[i][j]=cnt
        return cnt

    def uniquePaths(self, m: int, n: int) -> int:
        self.temp = [[-1]*n for _ in range(m)]
        self.temp[0][0]=1
        return self.traverse(m-1,n-1)
        

def fun(args=None):
    sol = Solution()
    return sol.uniquePaths(int(input()),int(input()),)


if __name__=='__main__':
    print(fun())#input().split(',')))