#https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

from Leetcode.utils.utility import insertLevelOrder,TreeNode, is_leaf, printLevelOrder
def fun(arr):
    root = insertLevelOrder(arr, 0, len(arr))
    printLevelOrder(root)
    sol = Solution()
    return sol.maxAncestorDiff(root)

class Solution:
    def maxAncestorDiff(self, root:TreeNode) -> int:
        return self.maxdiff(root, local_max=int(root.val), local_min=int(root.val))
    
    def maxdiff(self, root: TreeNode, local_max: int, local_min: int):
        if root==None or root.val=='None':
            return 0
        if int(root.val) > local_max:
            local_max = int(root.val)
        if int(root.val) < local_min:
            local_min = int(root.val)
        if not is_leaf(root):
            print('not leaf -> ',root.val, max, min)
            return  max(self.maxdiff(root.left, local_max, local_min),\
                self.maxdiff(root.right, local_max, local_min))
        else:
            print('lval -> ', root.val, ' max -> ', local_max, '  min -> ', local_min)
            val1 = abs(int(local_max-local_min))
            # val2 = abs(int(int(root.val) - local_min))
            return val1
        



if __name__=='__main__':
    tcs = int(input())
    while(tcs>0):
        print('res -> ',fun(input().split(',')))
        tcs-=1



#8,3,10,1,6,None,14,None,None,4,7,13