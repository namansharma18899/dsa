from Leetcode.utils.utility import timer


@timer
def mySol(number):
    if isinstance(number, float):
        raise TypeError("Input value must be a 'int' type")
    if number <= 0:
        return 0
    res = 1
    while (res << 1) <= number:
        res <<= 1
    return res


@timer
def claimedSOl(number):
    if number<=0:
        return 0
    c = 1
    for i in range(number+1):
        if (2**i <=number):
            c=i
        else:
            return c


for index in range(100000, 1000000, 200000):
    mySol(index)
    claimedSOl(index)
    print('\n')