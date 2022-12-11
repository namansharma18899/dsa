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
    if i < n:
        if not arr[i].isnumeric():
            return None
        root = TreeNode(int(arr[i]))
        root.left = insertLevelOrder(arr, 2 * i + 1, n)
        root.right = insertLevelOrder(arr, 2 * i + 2, n)        
    return root

def printLevelOrder(root):
    h = height(root)
    for i in range(1, h+1):
        printCurrentLevel(root, i)
 
 
# Print nodes at a current level
def printCurrentLevel(root, level):
    if root is None:
        return
    if level == 1:
        print('Value -> ', root.val, end="\n")
    elif level > 1:
        printCurrentLevel(root.left, level-1)
        printCurrentLevel(root.right, level-1)

def height(node):
    if node is None:
        return 0
    else:
        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)
 
        # Use the larger one
        if lheight > rheight:
            return lheight+1
        else:
            return rheight+1

def is_leaf(root: TreeNode):
        if root==None or root.val=='None':
            return False  
        if (root.left==None and root.right==None):
            return True
        else:
            return False
