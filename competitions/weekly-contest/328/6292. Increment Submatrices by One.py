from Leetcode.utils.utility import timeit
"""
Intuition -> We only traverse the Array once, revrse enginner to find how we can do it in one iteration....

* check if a point exists in the vicinity of how many squares, --> [CLOSE] 

Shifting to binary search( bad idea, too many searches will end with the same result )

Issues with thought -> ....
"""

class Solution:
    @timeit
    def range_add_queries(self, n: int, queries):  # List[List[int]]) -> List[List[int]]:
        matrix = [[0] * n for index in range(0, n)]
        return matrix
    # @timeit
    # def range_add_queries(self, n: int, queries):  # List[List[int]]) -> List[List[int]]:
    #     matrix = [[0] * n for index in range(0, n)]
    #     for each in queries:
    #         ri, ci = each[0], each[1]
    #         r2, c2 = each[2], each[3]
    #         for index in range(ri, r2 + 1):
    #             for col in range(ci, c2 + 1):
    #                 matrix[index][col] += 1
    #         print(matrix)
    #     return matrix

    def __repr__(self):
        return f'calc_object:{id(self)}'


def fun():
    sol = Solution()
    args = [[1, 1, 2, 2], [0, 0, 1, 1]]
    return sol.range_add_queries(int(input()), args)


if __name__ == '__main__':
    print(fun())  # input().split(',')))
