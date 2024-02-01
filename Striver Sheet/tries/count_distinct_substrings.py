from icecream import ic


class TrieNode:
    def __init__(self, text=""):
        self.children = {}
        self.is_eow = False


class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for i, char in enumerate(word):
            if char not in current.children:
                prefix = word[0 : i + 1]
                current.children[char] = TrieNode(prefix)
            current = current.children[char]
        current.is_eow = True

    def find_unique_substrings(self, node):
        result = 0
        def _traverse_trie_for_unique(node):
            if node is None:
                return 0
            res = 0
            for k, v in node.children.items():
                res += _traverse_trie_for_unique(v)
            return 1 + res
        for key, nodeval in node.children.items():
            result += _traverse_trie_for_unique(nodeval)
        return result+1


string = 'abab'
trie = PrefixTree()
for index, each in enumerate(string):
    trie.insert(string[index:])


ic(trie)
print(trie.find_unique_substrings(trie.root))

# Python program to concatenate two strings using
# rope data structure.
# Maximum no. of characters to be put in leaf nodes