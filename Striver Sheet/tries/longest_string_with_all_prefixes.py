class TrieNode:
    def __init__(self, char=""):
        self.children = {}
        self.char = char
        self.is_end_of_any_word = False
        self.count = 0


def insert_word(root, word):
    node = root
    for char in word:
        if char not in node.children:
            node.children[char] = TrieNode(char=char)
        node = node.children[char]
    node.is_end_of_any_word = True


def find_longest(node: TrieNode) -> int:
    if not node.is_end_of_any_word:
        return ""
    result = ""
    for _, each in node.children.items():
        res_word = find_longest(each)
        if len(res_word) == len(result):
            result = min(res_word, result)
        else:
            result = max(res_word, result)
    return node.char + "" + result


def longest_common_prefix(strings):
    if not strings:
        return ""
    root = TrieNode()
    for string in strings:
        insert_word(root, string)
    result = ""
    for _, node in root.children.items():
        res_word = find_longest(node)
        if len(res_word) == len(result):
            result = min(res_word, result)
        else:
            result = result if len(result) > len(res_word) else res_word
    return result if len(result) > 1 else None


# Example usage:
# string_list = ["apple", "apricot", "apology", "app"]
string_list = "g a ak szhkb hy".split(" ")
# string_list = "n ni nin ninj ninja ninga".split(' ')
# string_list = [ "ab" , "abc" , "a" , "bp"]
result = longest_common_prefix(string_list)

print(f"The longest common prefix is: {result}")
