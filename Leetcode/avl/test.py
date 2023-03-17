class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        self.root = self._insert(self.root, key)
        
    def _insert(self, node, key):
        if not node:
            return AVLNode(key)
        elif key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        
        node.height = 1 + max(self._height(node.left), self._height(node.right))
        
        balance = self._balance(node)
        
        # Left Left Case
        if balance > 1 and key < node.left.key:
            return self._right_rotate(node)
        
        # Right Right Case
        if balance < -1 and key > node.right.key:
            return self._left_rotate(node)
        
        # Left Right Case
        if balance > 1 and key > node.left.key:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        
        # Right Left Case
        if balance < -1 and key < node.right.key:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)
        
        return node
    
    def _height(self, node):
        if not node:
            return 0
        
        return node.height
    
    def _balance(self, node):
        if not node:
            return 0
        
        return self._height(node.left) - self._height(node.right)
    
    def _right_rotate(self, z):
        y = z.left
        T3 = y.right
        
        y.right = z
        z.left = T3
        
        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        
        return y
    
    def _left_rotate(self, z):
        y = z.right
        T2 = y.left
        
        y.left = z
        z.right = T2
        
        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        
        return y

    def midOrder(self):
        self._middleorder(self.root)

    def _middleorder(self, root):
        queue = ([root] if root else [])
        ln = len(queue)
        while(queue):
            while(ln>0):
                el = queue.pop(0)
                if not el:
                    ln-=1
                    continue
                queue.append(el.left if el.left else None)
                queue.append(el.right if el.right else None)
                print(el.key,end=" ")
                ln-=1
            print("\n")
            ln=len(queue)
        


    def preorder(self):
        self._preorder(self.root)
        
    def _preorder(self, node):
        if not node:
            return
        
        print("{0} ".format(node.key), end="")
        self._preorder(node.left)
        self._preorder(node.right)

def avl_from_array(arr):
    avl_tree = AVLTree()
    for i in arr:
        avl_tree.insert(i)
    return avl_tree

# Example usage
arr = [10, 20, 30, 40, 50, 25]
avl_tree = avl_from_array(arr)
avl_tree.midOrder() # should print: 30 20 10 25 40 50
