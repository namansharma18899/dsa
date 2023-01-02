# https://leetcode.com/problems/range-sum-of-bst/submissions/855888177/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root:TreeNode, low: int, high: int) -> int:
        if root==None:
            return 0
        sum = 0
        sum+=self.rangeSumBST(root.left, low, high)
        sum+=self.rangeSumBST(root.right, low , high)
        if root.val>=low and root.val<=high:
            sum+=root.val
        return sum