# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        count = 0
        if root.val==targetSum:
            count+=1
        return count+ self.psum(root.left, targetSum, root.val) + self.psum(root.right, targetSum, root.val)

    def psum(self, root, target, psum):
        if not root:
            return 0
        count = 0
        if root.val==target:
            count+=1
        if root.val + psum==target:
            count+=1
        # skip
        r1 = self.psum(root.left, target, root.val)
        r2 = self.psum(root.right, target, root.val)
        # use
        r3 = self.psum(root.left, target,  psum + root.val)
        r4 = self.psum(root.right, target, psum + root.val)

        return count + r1+r2+r3+r4