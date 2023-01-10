# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        res = [root.val]
        if root.left is not None:
            res+=self.preorderTraversal(root.left)
        if root.right is not None:
            res+=self.preorderTraversal(root.right)
        return res