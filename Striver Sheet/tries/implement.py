"""
implementing tries:

( foo, bar, barz, baz )
"""

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