class TrieNode:
    def __init__(self, text=""):
        self.children = {}
        self.ending = False


class PrefixTree:
    def __init__(self):
        self.root = TrieNode()
        self.root.ending=True

    def insert(self, word):
        current = self.root
        for i, char in enumerate(word):
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.ending = True

    def longest_str_with_all_prefixes(self, root):
        if not root.ending:
            return None
        mx = '' 
        for k,v in root.children.items():
            res = self.longest_str_with_all_prefixes(v)
            if res:
                res=k+' '+res
            else:
                res=''
            mx = res if len(res) > len(mx) else mx
        return mx



x = PrefixTree()
x.insert("arz")
x.insert("arm")
x.insert("a")
x.insert("ar")
result = x.longest_str_with_all_prefixes(x.root)
# print('asfdad')
print('onei' if result=='' else result)