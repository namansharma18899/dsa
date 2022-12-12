import numbers
from utils.utility import TreeNode, insertLevelOrder
# Definition for a binary tree node.

class Solution:
    def minOperations(self,arr1, arr2, i, j):        
        # Base Case
        if arr1 == arr2:
            return 0
            
        if i >= len(arr1) or j >= len(arr2):
            return 0
        
        # If arr[i] < arr[j]
        if arr1[i] < arr2[j]:
            
            # Include the current element
            return 1 \
            + self.minOperations(arr1, arr2, i + 1, j + 1)
        # Otherwise, excluding the current element
        return max(self.minOperations(arr1, arr2, i, j + 1),
                self.minOperations(arr1, arr2, i + 1, j))

    def minOperationsUtil(self,arr):     
        brr = sorted(arr,reverse=True)  
        if(arr == brr):
           return 0
        else:
            return self.minOperations(arr, brr, 0, 0)


    def find_minimum(self, arr):
        if len(arr)==1:
            return 0
        arr = [int(node.val) for node in arr if isinstance(node.val, numbers.Number)]
        return self.minOperationsUtil(arr)

    def minimumOperations(self, root:TreeNode) -> int:
        #level order traversal
        if root==None:
            return None
        queue = list()
        queue.append(root)
        size = len(queue)
        ops = 0
        while(size > 0):
            while(size > 0):
                node = queue.pop(0)
                # print('val >', node.val, node.left, node.right)
                if node.left:
                    # print('not none ->',node.left)
                    queue.append(node.left)
                if node.right:
                    # print('not none ->',node.right)
                    queue.append(node.right)
                size-=1
            ops+=self.find_minimum(queue)
            size = len(queue)
        return ops


def fun(args):
    root_node = insertLevelOrder(args,0,len(args))
    sol = Solution()
    return (sol.minimumOperations(root=root_node))


if __name__=='__main__':
    # print(fun(input().split(',')))
    sol = Solution()
    arr = [27,29,17]
    print(sol.minOperationsUtil(arr))