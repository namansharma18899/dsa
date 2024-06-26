from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        left_depth = self.diameterOfBinaryTree(root.left)
        right_depth = self.diameterOfBinaryTree(root.right)
        self.diameter = max(self.diameter, left_depth+right_depth)
        return max(left_depth, right_depth)