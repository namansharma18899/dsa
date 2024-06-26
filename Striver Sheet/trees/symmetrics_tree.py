# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.check_sym(root.left, root.right)

    def check_sym(self, n1, n2):
        if None in [n1,n2]: 
            if n1 is not None or n2 is not None:
                return False
            return True
        if n1.val!=n2.val:
            return False
        return False if False in [self.check_sym(n1.left, n2.right), self.check_sym(n1.right, n2.left)] else True
