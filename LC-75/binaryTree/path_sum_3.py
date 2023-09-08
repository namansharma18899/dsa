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
        if root.right and root.right.val == targetSum:
            count+=1
        if root.left and root.left.val == targetSum:
            count+=1
        res = self.psum(root.left, targetSum, root.val) + self.psum(root.right, targetSum, root.val)
        return count + res

    def psum(self, root, target, psum):
        if not root:
            return 0
        count = 0
        if root.val + psum==target:
            print('root + target', root.val, psum)
            count+=1
        # skip
        if root.left and root.left.val == target:
            count+=1
        r1 = self.psum(root.left, target, root.val)
        r3 = self.psum(root.left, target, psum + root.val)
        # use
        if root.right and root.right.val == target:
            count+=1
        r2 = self.psum(root.right, target, root.val)
        r4 = self.psum(root.right, target, psum + root.val)

        return count + r1+r2+r3+r4       

x = Solution()
arr = [1,None,2,None,3,None,4,None,5]

