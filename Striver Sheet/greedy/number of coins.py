from os import *
from sys import *
from collections import *
from math import *

denominations = [1, 2, 5, 10, 20, 50, 100, 500, 1000]


def findMinimumCoins(amount):
    count = 0
    den = sorted(denominations, reverse=True)
    for each in den:
        if each > amount:
            continue
        if amount <= 0:
            break
        count += int(amount / each)
        amount = amount % each
    return count


if __name__ == '__main__':
    amount = int(input())
    print(findMinimumCoins(amount))
