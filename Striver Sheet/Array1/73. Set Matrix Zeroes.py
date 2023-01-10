class Solution:
    def setZeroes(self, matrix):#: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        visited_col = set()
        for row in range(0,len(matrix)):
            row_convert = False
            if 0 in matrix[row]:
                row_convert=True
            for col in range(0,len(matrix[row])):
                if matrix[row][col]==0:
                    visited_col.add(col)
                elif row_convert is True:
                    matrix[row][col]=0
        for each in visited_col:
            for row in range(0,len(matrix)):
                matrix[row][each]=0
        
    