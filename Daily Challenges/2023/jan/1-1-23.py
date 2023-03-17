#from utils import *
import random
class Solution:
    def wordPattern(self, pattern: str, word: str) -> bool:
        word = word.split(' ')
        if len(pattern)!=len(word):
            return False
        keyval = {}
        patter_index = 0
        visited = set()
        for index in range(0,len(word)):
            char = word[index]
            curr_pattern_char=pattern[index]
            if char not in visited:
                visited.add(char)
                if not curr_pattern_char not in keyval:
                    return False
                else:
                    keyval[curr_pattern_char]=char
            else:
                try:
                    if keyval[curr_pattern_char]!=char:
                        return False
                except Exception as e:
                    return False
        return True

        
        # for i in range(0,len(word)-len(pattern)+1):
        #     if self.checkPattern(word,i,i+len(pattern),pattern):
        #         return True
        # return False

    def checkPattern(self,arr,start,end,pattern):
        keyval = {}
        patter_index = 0
        visited = set()
        for index in range(start,end):
            char = arr[index]
            curr_pattern_char=pattern[patter_index]
            if char not in visited:
                visited.add(char)
                if not curr_pattern_char not in keyval:
                    return False
                else:
                    # pattern[patter_index]
                    keyval[curr_pattern_char]=char
            else:
                # pattern[patter_index]
                try:
                    if keyval[curr_pattern_char]!=char:
                        return False
                except Exception as e:
                    return False
            patter_index+=1
        return True

def fun():
    sol = Solution()
    pattern = input()
    string = str(input())
    # for i in range(0,len(string)-len(pattern)+1):
    #         if sol.checkPattern(string,i,i+len(pattern),pattern):
    #             return True
    return sol.wordPattern(pattern,string)


if __name__=='__main__':
    print(fun())