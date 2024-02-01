# ROPE_STR_SIZE = 3


# class RopeNode:
#     def __init__(self, value, left=None, right=None, weight=0):
#         self.value = value
#         self.left = left
#         self.right = right
#         self.weight = weight


# def build_rope(sstr: str):
#     if len(sstr) >= ROPE_STR_SIZE:
#         left_node = build_rope(sstr[:ROPE_STR_SIZE])
#         right_node = build_rope(sstr[ROPE_STR_SIZE:])


# def index(rope, i):
#     if rope is None:
#         return None

#     if i < 0 or i >= rope.weight:
#         raise IndexError("Index out of range")

#     if rope.left is None and rope.right is None:
#         return rope.value[i]

#     if i < rope.left.weight:
#         return index(rope.left, i)
#     else:
#         return index(rope.right, i - rope.left.weight)


# def concatenate(rope1, rope2):
#     if rope1 is None:
#         return rope2
#     elif rope2 is None:
#         return rope1

#     new_value = rope1.value + rope2.value
#     new_weight = rope1.weight + rope2.weight

#     return RopeNode(value=new_value, left=rope1, right=rope2, weight=new_weight)


# # Example Usage:
# string1 = "Hello, "
# string2 = "world!"

# rope1 = build_rope(string1)
# rope2 = build_rope(string2)
# print(index(concatenated_rope, i), end="")
# print("hell")


LEAF_LEN = 2


# Rope structure
class Rope:
    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None
        self.str = [0] * (LEAF_LEN + 1)
        self.lCount = 0


# Function that creates a Rope structure.
# node --> Reference to pointer of current root node
# a --> input String
# l --> Left index of current substring (initially 0)
# r --> Right index of current substring (initially n-1)
# par --> Parent of current node (Initially NULL)
def createRopeStructure(node, par, a, l, r):
    tmp = Rope()
    tmp.left = tmp.right = None

    # We put half nodes in left subtree
    tmp.parent = par

    # If string length is more
    if (r - l) > LEAF_LEN:
        tmp.str = None
        tmp.lCount = (r - l) // 2
        node = tmp
        m = (l + r) // 2
        createRopeStructure(node.left, node, a, l, m)
        createRopeStructure(node.right, node, a, m + 1, r)
    else:
        node = tmp
        tmp.lCount = r - l
        j = 0
        for i in range(l, r + 1):
            print(a[i], end="")
            tmp.str[j] = a[i]
            j = j + 1
        print(end="")

    return node


# Function that prints the string (leaf nodes)
def printstring(r):
    if r == None:
        return

    if r.left == None and r.right == None:
        # console.log(r.str);
        pass
    printstring(r.left)
    printstring(r.right)


# Function that efficiently concatenates two strings
# with roots root1 and root2 respectively. n1 is size of
# string represented by root1.
# root3 is going to store root of concatenated Rope.
from Leetcode.utils.utility import timer


# @timer
def concatenate(root3, root1, root2, n1):
    # Create a new Rope node, and make root1
    # and root2 as children of tmp.
    tmp = Rope()
    tmp.left = root1
    tmp.right = root2
    root1.parent = tmp
    root2.parent = tmp
    tmp.lCount = n1

    # Make string of tmp empty and update
    # reference r
    tmp.str = None
    root3 = tmp
    return root3


@timer
def oldschool_join(s1, s2):
    s3 = s1 + s2
    return s3

root1 = None

from sys import stdin
from random import choice
from string import ascii_lowercase

a = "Hi This is geeksforgeeks. "
n1 = len(a)
root1 = createRopeStructure(root1, None, a, 0, n1 - 1)

# Create a Rope tree for second string
root2 = None
b = "You are welcome here."
n2 = len(b)
root2 = createRopeStructure(root2, None, b, 0, n2 - 1)

root3 = None
root3 = concatenate(root3, root1, root2, n1)
printstring(root3)
print()
# t3 = oldschool_join(a,b)
