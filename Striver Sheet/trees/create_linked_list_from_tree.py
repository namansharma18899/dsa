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
        def flatten_tree(root):
            if not root:
                return None
            left_subtree_rmost_child = flatten_tree(root.left)
            right_subtree_rmost_child = flatten_tree(root.right)
            if left_subtree_rmost_child:
                left_subtree_rmost_child.right = root.right
                root.right = root.left
                root.left = None
                return right_subtree_rmost_child if right_subtree_rmost_child else left_subtree_rmost_child
            return root if not right_subtree_rmost_child else right_subtree_rmost_child
        head = root
        flatten_tree(root)