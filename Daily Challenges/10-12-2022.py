#https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/
from Leetcode.utils.utility import TreeNode, is_leaf, insertLevelOrder
    
def fun(arr):
    #get sum of all elements in the tree
    root = insertLevelOrder(arr,0,len(arr))
    sum_tree = sum_tree_values(root)
    # get individual sum of subtrees
    sol = Solution()    
    sol.max_product(root, sum_tree)
    return sol.max_p
class Solution:
    max_p = 0
    def max_product(self,root, sum_tree):
        if root==None or root.val=='None':
            return 0
        curr_sub_tree_sum = int(root.val) + self.max_product(root.left, sum_tree) + \
            self.max_product(root.right, sum_tree)
        if (curr_sub_tree_sum * int(sum_tree - curr_sub_tree_sum) > self.max_p):
            self.max_p = curr_sub_tree_sum * int(sum_tree - curr_sub_tree_sum)
        return root.val

def sum_tree_values(root: TreeNode):
    if root==None or root.val=='None':
        return 0
    else:
        val =  root.val + sum_tree_values(root.left) + sum_tree_values(root.right)
        return val


if __name__=='__main__':
    tcs = int(input())
    while(tcs>0):
        print('res -> ',fun(input().split(',')))
        tcs-=1