# class Solution:
from collections import Counter


def equalFrequency( word: str) -> bool:
    freq= {}
    # for index in range(len(word)-2):
    #     print('this -> ',word[:index],word[index+1:])
    #     if len(set((Counter(word[0:index]+word[index+1:]).values())))==1:
    #         return True
    counter = Counter(word) # O(N) time
    for c in word:
        print(c, counter)
        counter[c] -= 1
        
        if counter[c] == 0:
            counter.pop(c)
        print(set(counter.values()))
        if len(set(counter.values())) == 1:
            return True

        counter[c] += 1
    return False
        
print(equalFrequency(input()))