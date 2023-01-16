
# Definition for a binary tree node.
from Leetcode.utils.utility import insertLevelOrder, TreeNode

# class TreeNode:
#     def __init__(self, val=None, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root):# Optional[TreeNode]) -> bool:
        pass


def fun(args):
    sol= Solution()
    Root = insertLevelOrder(args,0,len(args))
    return sol.isSymmetric(Root)


if __name__=='__main__':
    tcs = int(input())
    while(tcs>0):
        print('res -> ',fun(input().split(',')))
        tcs-=1