from typing import List

arr = [[1, 2, 3], [4, 5, 6]]


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        def traverse_2d_array(grid, i, j):
            if i>=self.row or j>=self.col:
                return None
            if self.dp_arr[i][j] == None:
                # traverse
                move_l = traverse_2d_array(grid, i, min(self.col-1, j+1))
                move_d = traverse_2d_array(grid, min(self.row-1, i+1), j)
                if move_l==None and move_d==None: #bottom corner
                    self.dp_arr[i][j] = self.grid[i][j]
                else:
                    self.dp_arr[i][j] = grid[i][j] + min(move_l if move_l else 999900,move_d if move_d else 999900)
            return self.dp_arr[i][j] 

        self.row, self.col = len(grid), len(grid[0])
        self.dp_arr = [[None]*self.col for _ in range(self.row)]
        traverse_2d_array(grid, 0,0)
        return 0
