from typing import List
"""
Below is the wrong approach because the endcondition is not specified...
The solution for one branch of the tree is half baked.

ps: I'll try to write this down by myself tomorrow.
"""

# class Solution:
#     def partition(self, s: str) -> List[List[str]]:
#         temp = list()
#         def check(sub, ind):
#             if sub!=sub[::-1]:
#                 return False
#             p = ind+1
#             temp.append(sub)
#             while(p < len(s)):
#                 s1 = sub[:part]
#                 if check(s1, 1):
#                     temp.append(s1)
#                 s2 = sub[part:]
#                 if check(s2, 1):
#                     temp.append(s2)
#                 p+=1
                

#         res = []
#         part = 1 
#         while(part<len(s)):
#             temp = []
#             s1 = s[:part]
#             s2 = s[part:]
#             temp = []
#             check(s1, 1)
#             res.append(temp+[])
#             temp = []
#             check(s2, 1)
#             res.append(temp+[])
#             part+=1
