import numpy as np
#from utils import *
class Solution:
    def rotate(self,matrix):# List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # temprary array for storing residual rows
        level = 0
        top, bottom, right, left = 0, len(matrix)-1, len(matrix)-1,0
        while(level< len(matrix)/2):
            try:
                temp = [matrix[index][left] for index in range(top,bottom+1)][::-1] #reverse
                for index in range(top,bottom+1):
                    matrix[index][left] = matrix[bottom][index]
                for i,j in zip(range(left,right+1), range(bottom,top-1,-1)):
                    matrix[bottom][i]=matrix[j][right]
                for index in range(bottom,top-1,-1):
                    matrix[index][right]=matrix[top][index]
                for index in range(left,right+1):
                    matrix[top][index] = temp.pop(0)
                # self.matrix[top:bottom,left]=self.matrix[bottom-1,[x for x in range(left,right)]]
                # self.matrix[bottom-1,[x for x in range(left,right)]] = self.matrix[top:bottom,right-1][::-1] 
                # self.matrix[top:bottom,right-1] = self.matrix[top,[x for x in range(left,right)]]
                # self.matrix[top,[x for x in range(left,right)]] = temp
                # self.matrix[top][right-1]=temp[-1]
            except Exception as err:
                print(err)
            top+=1
            left+=1
            bottom-=1
            right-=1
            level+=1
        print(matrix)
        return matrix

def fun():
    args =[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    sol = Solution()
    print(sol.rotate(args))
    # sol.matrix)
    # return res


if __name__=='__main__':
    print(fun())