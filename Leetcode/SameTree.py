from utils.utility import insertLevelOrder,TreeNode

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        try:
            if p.val==q.val:
                res1 = self.isSameTree(p.left, q.left)
                res2 = self.isSameTree(p.right, q.right)
                return True if res1==True and res2==True else False
        except Exception as e:
            if p==None and q==None:
                return True
        return False

