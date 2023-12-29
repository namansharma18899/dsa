"""
implementing tries:

( foo, bar, barz, baz )
"""
from collections import defaultdict
import os

class Trie:
    def __init__(self):
        self.root = dict()
        

    def insert(self, word: str) -> None:
        root = dict(self.root)
        _end = '_end_'
        def make_trie(*words):
            for word in words:
                current_dict = root
                for letter in word:
                    current_dict = current_dict.setdefault(letter, {})
                current_dict[_end] = _end
            return root
        self.root.update(make_trie(word))

    def search(self, word: str) -> bool:
        curr = self.root
        for letter in word:
            if letter not in curr.keys():
                return False
            curr = curr[letter]
        return '_end_' in curr 

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for letter in prefix:
            if letter not in curr.keys():
                return False
            curr = curr[letter]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

class TrieNode:
    def __init__(self, text=''):
        self.children = {}
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
            current = current.children[char]
        current.is_eow = True

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


if __name__ == "__main__":
    obj = PrefixTree()
    obj.insert("apple")
    obj.insert('apraisel')
    obj.insert('absolute')
    obj.insert('blink')
    obj.insert('bloke')
    print(obj.start_with(word='app'))
