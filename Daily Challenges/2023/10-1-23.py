# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        try:
            if p.val==q.val:
                res1 = self.isSameTree(p.left, q.left)
                res2 = self.isSameTree(p.right, q.right)
                return True if res1==True and res2==True else False
        except Exception as e:
            if p==None and q==None:
                return True
        return False