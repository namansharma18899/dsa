from copy import deepcopy


class Solution:
    def solveNQueens(self, n: int):
        # arr = [[0]*n]*n
        arr = [[0 for x in range(n)] for _ in range(n)]
        affected = []
        result = []

        def update_affected(row, col, affect=True):
            for r_tmp in range(0, n): # Entire Column
                arr[r_tmp][col] = arr[r_tmp][col]+2 if affect else arr[r_tmp][col]-2
            for col_tmp in range(0, n): # Entire ROW
                arr[row][col_tmp] = arr[row][col_tmp]+2 if affect else arr[row][col_tmp]-2
            row_tmp = row-1
            for col_tmp in range(col+1, n): #top right
               if row_tmp not in range(0,n):
                   break
               arr[row_tmp][col_tmp] = arr[row_tmp][col_tmp]+2 if affect else arr[row_tmp][col_tmp]-2 
               row_tmp-=1
            row_tmp= row+1
            for col_tmp in range(col+1, n): #bottm right
                if row_tmp not in range(0,n):
                   break
                arr[row_tmp][col_tmp] = arr[row_tmp][col_tmp]+2 if affect else arr[row_tmp][col_tmp]-2 
                row_tmp+=1
            row_tmp= row-1
            for col_tmp in range(col-1, -1, -1): #bottm right
               if row_tmp not in range(0,n):
                   break
               arr[row_tmp][col_tmp] = arr[row_tmp][col_tmp]+2 if affect else arr[row_tmp][col_tmp]-2
               row_tmp-=1
            row_tmp= row+1
            for col_tmp in range(col-1, -1, -1): #bottm right
               if row_tmp not in range(0,n):
                   break
               arr[row_tmp][col_tmp] = arr[row_tmp][col_tmp]+2 if affect else arr[row_tmp][col_tmp]-2 
               row_tmp+=1
 
        def solve(i, j, count):
            if count == n:
                res = []
                for i_tmp in range(n):
                    st = ""
                    for j_tmp in range(n):
                        st+= 'Q' if arr[i_tmp][j_tmp]==1 else '.' 
                    res.append(st)
                result.append(res)
                return
            if i >= n or j >= n:
                return
            for row in range(i, n):
                for col in range(j, n):
                    if arr[row][col]!=0:  # affected
                        continue
                    update_affected(row, col, True)
                    arr[row][col] = 1  # make it a queen
                    solve(row + 1, 0, count + 1)
                    update_affected(row, col, False)
                    arr[row][col] = 0

        solve(0, 0, 0)
        return result


sol = Solution()


print(sol.solveNQueens(int(input())))
