# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return 1 + self.good(root.left, root.val) + self.good(root.right, root.val)
    
    def good(self, root, maxtb):
        if not root:
            return 0
        if root.val >= maxtb:
            return 1+self.good(root.left, root.val) + self.good(root.right, root.val)
        else:
            return self.good(root.left, maxtb) + self.good(root.right, maxtb)
