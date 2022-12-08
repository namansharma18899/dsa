# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def leaf(self,root: TreeNode):
        if root.left==None and root.right==None:
            return True
        else:
            return False
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        arr1 = self.get_leaf_nodes(root1)
        arr2= self.get_leaf_nodes(root2)
        # for each in arr1:
            # if each is not None:
            #     print('val -> ', each.val)
            # else:
            #     print('nonee')
        arr1 = [int(element.val) for element in arr1]
        arr2 = [int(element.val) for element in arr2]
        return True if arr1==arr2 else False

    def get_leaf_nodes(self,root):
        if root==None:
            return []
        if self.leaf(root):
            return [root.val]
        result = []
        result+=self.get_leaf_nodes(root.left)
        result+=self.get_leaf_nodes(root.right)
        return result
        # if self.leaf(root1) or self.leaf(root2):
        #     print('leaf -> ', root1.val, root2.val)
        #     try:
        #         if int(root1.val) == int(root2.val):
        #             print(root1.val)
        #             return True
        #         return False
        #     except Exception as e:
        #         return False
        # else:
        #     return True if self.leafSimilar(root1.left, root2.left) \
        #         or self.leafSimilar(root1.right, root2.right) else False
        # return True if result_left_subtree or result_right_subtree else False


def fun(arr):
    from Leetcode.utils.utility import insertLevelOrder
    root = insertLevelOrder(arr, 0, len(arr))
    root2 = insertLevelOrder(input().split(','), 0, len(arr))
    sol = Solution()
    return sol.leafSimilar(root1=root, root2=root2)

if __name__=='__main__':
    tcs = int(input())
    while(tcs>0):
        print('res -> ',fun(input().split(',')))
        tcs-=1