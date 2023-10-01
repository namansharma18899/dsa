from math import *
from collections import *
from sys import *
from os import *

def missingAndRepeating(arr, n):
    rep = None
    for index in range(n):
        el = arr[index]
        if el<0:
            el = -1 * el
        if arr[el-1]<0:
            rep = el
            continue
        arr[el-1]=-1 * arr[el-1]
    for index in range(n):
        if arr[index]>0:
            return index+1, rep