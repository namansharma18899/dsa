import math
"""
HINT: Merge Sort Algorithm
"""

arr= [14, 7, 3, 12, 9, 11, 6, 2]
# arr = [14, 2, 3 ,12]


def find_inversions(arr):
    # count = merge_sort(arr, 0, len(arr)-1) 
    count = msort(arr)
    print(arr)
    return count
    

def msort(arr):
    if len(arr)>1:
        mid_point = len(arr)//2
        L = arr[:mid_point]
        R = arr[mid_point:]
        res = 0
        res+=msort(L)
        res+=msort(R)
        i,j,k=0,0,0
        while(i<len(L) and j<len(R)):
            if L[i] > R[j]:
                arr[k]=L[i]
                res+=len(R) - j
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1
        while(i<len(L)):
            arr[k] = L[i]
            i+=1
            k+=1
        while(j<len(R)):
            arr[k]=R[j]
            j+=1
            k+=1
        return res
    return 0

print(find_inversions(arr))