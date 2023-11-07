from copy import deepcopy


class Solution:
    def solveNQueens(self, n: int):
        # arr = [[0]*n]*n
        arr = [[0 for x in range(n)] for _ in range(n)]
        affected = []
        result = []

        def update_affected(row, col, affect=True):
            for r_tmp in range(0, n):
                arr[r_tmp][col] = 2 if affect else 0
            for col_tmp in range(0, n):
                arr[row][col_tmp] = 2 if affect else 0
            row_tmp = row-1
            for col_tmp in range(col+1, n): #top right
               arr[row_tmp][col_tmp] = 2 
               row_tmp-=1
            row_tmp= row+1
            for col_tmp in range(col+1, n): #bottm right
               arr[row_tmp][col_tmp] = 2 
               row_tmp+=1
            row_tmp= row-1
            for col_tmp in range(col-1, -1, -1): #bottm right
               arr[row_tmp][col_tmp] = 2 
               row_tmp-=1
            row_tmp= row+1
            for col_tmp in range(col-1, -1, -1): #bottm right
               arr[row_tmp][col_tmp] = 2 
               row_tmp+=1
 
        def solve(i, j, count):
            if count == n:
                tmp = deepcopy(arr)
                result.append(tmp)
                return
            if i >= n or j >= n:
                return
            for row in range(i, n):
                for col in range(j, n):
                    if arr[row][col] == 2:  # affected
                        continue
                    update_affected(row, col, True)
                    arr[row][col] = 1  # make it a queen
                    solve(i + 1, 0, count + 1)
                    update_affected(row, col, False)

        solve(0, 0, 0)
        return result


sol = Solution()


print(sol.solveNQueens(int(input())))
