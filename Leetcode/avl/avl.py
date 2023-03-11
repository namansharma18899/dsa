from Leetcode.utils.utility import print_tree

class AVLNode:
    def __init__(self,key) -> None:
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def avl_from_array(arr: list) -> None:
    avlTree = AVLTree()
    for each in arr:
        avlTree.insert(each)


class AVLTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, key):
        self._insert(node=self.root,key=key)

    def _insert(self,node,key):
        if not node:
            return AVLNode(key=key)
        elif key<=node.key:
            node.left= self._insert(node.left,key)
        else:
            node.right = self._insert(node.right, key)
        """the tree might get imbalanced by adding this new node...
        if its the case we might need to rotate it """
        node.height = 1+ (max(node.left.height if node.left else 0, node.right.height if node.right else 0))
        
        balance = self._check_balance(node)
        if balance >1:
            """
            Left balance
            """
            # to see if we can left blance -> 
            if node.left.right:
                """
                right balance
                """
                self._right_rotate(node.left)
            self._left_rotate(node)
        elif balance <1:
            pass
        return node

#TODO: COMPLETE LEFT & RIGHT ROTATE
    def _left_rotate(self,node):
        pass


    def _right_rotate(self, node):
        pass


    def _check_balance(self, node):
        if not node:
            return 0
        return ((node.left.height if node.left else 0) - (node.right.height if node.right else 0))

    def __repr__(self):
        return print_tree(self.root)


if __name__=='__main__':
    array = [int(x) for x in input().split(' ')]
    avl = AVLTree()
    avl_from_array(array)
    print(avl)