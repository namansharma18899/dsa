"""
implementing tries:

( foo, bar, barz, baz )
"""

from collections import defaultdict



_end = '_end_'

root = dict()

def make_trie(*words):
    for word in words:
        current_dict = root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict[_end] = _end
    return root

def search(word):
    curr_dict = root
    for letter in word:
        if letter not in curr_dict.keys():
            return False
        curr_dict = curr_dict[letter]
    return _end in curr_dict

print(make_trie('namaste', 'name', 'naman', 'sharp', 'shape'))

print(search('name'))