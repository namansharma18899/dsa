class Node:
    def __init__(self, val: str, left= None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right
        

class STree:
    def __init__(self, text: str) -> None:
        self.text = text
        self.root = Node(val='')
 
    def construct_s_tree(self):
        temp = self.text + ''
        for index in range(len(temp)-1, -1 , -1):
            char = temp[index:]
            if self.bfs(self.root, char):
                # found
                pass
            else:
                pass

    def bfs(self,root: Node, txt: str):
        if not root:
            return None
        if  root.val[0]==txt:
            return root
        v1 = self.bfs(root.left, txt)
        v2 = self.bfs(root.right, txt)
        if v1 or v2:
            return v1 if v1 else v2
        return None
        
