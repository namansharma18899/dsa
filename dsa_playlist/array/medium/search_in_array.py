arr, target = [[1,3,5,7],[10,11,16,20],[23,30,34,60]],  3

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        w,h = len(matrix), len(matrix[0])
        def search_element(target):
            cur_row = 0
            cur_col = 0
        return search_element(target)#, i=0, j=0)