arr =[
    [4,9,7],
    [3,8,5],
    [1,2,6]
]

class Solution:
    def traverse(self,prev, i,j):  
        if self.temp[i][j]!=-1:
            self.temp[i][j] = min(prev+arr[i][j], self.temp[i][j])
        else:
            self.temp[i][j] = prev+arr[i][j]
        prev = prev + arr[i][j]
        if i>0:
            self.traverse(prev, i-1,j)
        if j>0:
            self.traverse(prev, i,j-1)

    def uniquePaths(self, arr):
        m = len(arr)
        n = len(arr[0])
        self.temp = [[-1]*n for _ in range(m)]
        # self.temp[0][0]=1
        self.traverse(0,m-1,n-1)
        return self.temp[0][0]
        

def fun(args=None):
    sol = Solution()
    return sol.uniquePaths(arr)


if __name__=='__main__':
    print(fun())#input().split(',')))
