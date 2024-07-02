# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    head = None
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def flt(root):
            if not root:
                return
            if not self.head:
                head = root
            temp_r = root.right 
            temp_l = root.left 
            self.flatten(root.right)
            self.flatten(root.left)
            root.right = root.left
            root.left = None
            root.right.right = temp_r
        flt(root)