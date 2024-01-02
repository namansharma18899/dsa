class TrieNode:
    def __init__(self, text=''):
        self.children = {}
        self.count= 1
        self.is_eow = False


class PrefixTree:
    def __init__(self):
        self.root = TrieNode()


    def insert(self, word):
        current = self.root
        for i, char in enumerate(word):
            if char not in current.children:
                prefix = word[0:i+1]
                current.children[char] = TrieNode(prefix)
            else:
                current.children[char].count+=1
            current = current.children[char]
        current.is_eow = True
    
    def frequency(self, word: str):
        current = self.root
        for char in word:
            if char not in current.children:
                return 0
            current = current.children[char]
        return current.count
    
    def remove(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return 0
            current.children[char].count-=1
            current = current.children[char]
        return current.count
 

    def find(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_eow
    
    def start_with(self, word):
            node = self.root
            for char in word:
                if char not in node.children:
                    return False
                node = node.children[char]
            return True

    
x = PrefixTree()
x.insert("samsung")
x.insert("samsung")
x.insert("vivo")
x.remove("vivo")
print(x.frequency('samsung'))
print(x.frequency('vi'))