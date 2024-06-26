from typing import Optional


class TreeNode:
    def __init__(self, val) -> None:
        self.lm = 0
        self.rm = 0
        self.left = None
        self.right = None
        self.val = val



class Solution:
    global_max = -9999999999

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.get_max_sum(root)        
        return self.global_max

    def get_max_sum(self, root):
        if not root:
            return 0
        self.global_max = max(root.val, self.global_max)
        root.lm = max(0,self.get_max_sum(root.left))
        root.rm = max(0, self.get_max_sum(root.right))
        self.global_max = max(root.val+root.lm+root.rm, self.global_max)
        root.lm = 0 if not root.lm else root.lm
        root.rm = 0 if not root.rm else root.rm
        return max(root.val+root.lm, root.val + root.rm)