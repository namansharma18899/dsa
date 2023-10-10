"""
Complexity -> O(NxM) where N-> len str and M is avg len of word
"""
from Leetcode.utils.utility import timer


def swap(arr, l, r):
    while(l<r):
        temp = arr[l]
        arr[l] = arr[r]
        arr[r] = temp
        l+=1
        r-=1


class Solution:
    @timer
    def reverseWords(self, s: str) -> str:
        st = [x for x in s]
        swap(st, 0, len(st)-1)
        st = [x for x in ''.join(st).strip() ]
        start= 0
        mfd = list()
        for ind in range(len(st)+1):
            if ind==len(st):
                swap(st, start, ind-1)
                break
            if st[ind]== ' ':
                if st[ind-1]==' ':
                   mfd.append(ind) 
                else:
                    swap(st, start, ind-1)
            else:
                if ind>0 and st[ind-1]==' ':
                    start =ind
            ind+=1
        return ''.join([x for idx, x in enumerate(st) if idx not in mfd])

sol =Solution()

st = 'a good   example'

print(sol.reverseWords(st))