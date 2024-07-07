
'''

    Following is the Binary Tree node structure
    
    class BinaryTreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

'''

        
def update_values(root, is_root=False):
    if not root:
        return False
    rl = root.left.data if root.left else 0
    rr = root.right.data if root.right else 0
    if root.data <=  rl+rr:
        if is_root:
            root.data = rl+rr
            return True
        else:
            return False
    else:
        if rl < rr:
            root.left.data = min(rl+rr, root.data-rl+rr)
            root.right.data =  max(rl+rr, root.data-rl+rr)
        else:
            root.right.data =  min(rl+rr, root.data-rl+rr)
            root.left.data = max(rl+rr, root.data-rl+rr)
        update_values(root.left)
        update_values(root.right)

def changeTree(root): 
    # Write your code here.
    update_values(root)