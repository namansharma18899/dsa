# Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. That is, no letter appears in a single substring more than once.

# Return the minimum number of substrings in such a partition.

# Note that each character should belong to exactly one substring in a partition.

 

# Example 1:

# Input: s = "abacaba"
# Output: 4

import enum


def fun():
    s = "ss"
    kv = {}
    st = ''
    count = 1
    kv[s[0]]=1
    st+=s[0]
    for index,val in enumerate(s):
        if index>0:
            if val not in kv.keys():
                kv[val] = 1
                st+=val
            else:
                print(st)
                count+=1
                kv = {}
                kv[val] = 1
                st=''+val
    print(st)
    return count


print(fun())