from os import *
from sys import *
from collections import *
from math import *

"""
Intuition -> Stack, previx pointer to tell num greater...
"""


def getInversions(arr, n) :
	# Write your code here.
    arr = [2,5,1,3,4]

    return 1

# Taking inpit using fast I/O.
def takeInput() :
    n = int(input())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

# Main.
# arr, n = takeInput()
# print(getInversions(arr, n))


"""
2nd try 
"""

# def c_inversion(arr):
#     i = 0
#     j = len(arr)-1
#     count=0
#     while(i < j):
#         if arr[i] > arr[j]:
#             temp = j+0
#             while(i < temp and arr[i] >  arr[temp]):
#                 count+=1
#                 temp-=1
#         i+=1
#     return count

# arr = [2,5,1,3,4]
# print(c_inversion(arr))

def count_inversion(arr):
    i,j = 0, len(arr)-1 
    result = 0
    while(i<j):
        pass
    return result

arr = [3, 2, 1]
print(count_inversion(arr))