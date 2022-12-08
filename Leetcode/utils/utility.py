def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insertLevelOrder(arr, i, n):
    root = None
    # Base case for recursion 
    if i < n:
        root = TreeNode(arr[i])
        # insert left child 
        root.left = insertLevelOrder(arr, 2 * i + 1, n)
        # insert right child 
        root.right = insertLevelOrder(arr, 2 * i + 2, n)  
    return root