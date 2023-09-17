# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.result = 0
        self.dfs(root, targetSum)
        return self.result

    def dfs(self, node, targetSum):
        if not node:
            return
        #Preorder
        self.test(node, targetSum)
        self.dfs(node.left, targetSum)
        self.dfs(node.right, targetSum)

    def test(self, node: Optional[TreeNode], target: int):
        if not node:
            return
        if node.val==target:
            self.result+=1
        target-=node.val
        self.test(node.left,  target)
        self.test(node.right, target)



x = Solution()
arr = [1,None,2,None,3,None,4,None,5]
num= 3

print(x.pathSum(arr,num))
