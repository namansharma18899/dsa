from os import *
from sys import *
from collections import *
from math import *

denominations = [1, 2, 5, 10, 20, 50, 100, 500, 1000]


def findMinimumCoins(amount):
	count = 0
	x=sorted(denominations, reverse=True)
	for each in denominations:
		if amount<=0:
			break
		count+=int(amount/each)
		amount= amount%each
	return count


def fun():
    return findMinimumCoins(int(input()))


if __name__=='__main__':
    tcs = int(input())
    while(tcs>0):
        print('res -> ',fun())#nput().split(',')))
        tcs-=1