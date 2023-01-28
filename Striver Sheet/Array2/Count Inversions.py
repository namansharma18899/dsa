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
arr, n = takeInput()
print(getInversions(arr, n))