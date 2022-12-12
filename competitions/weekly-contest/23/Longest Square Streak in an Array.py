

from math import sqrt


def fun(args):
    nums = sorted(args)
    max = -999
    next_square = {each:1 for each in nums}
    for index, num in enumerate(nums):
        if not int(int(sqrt(num)) + 0.5) ** 2 == num:
            continue
        if int(sqrt(num)) in next_square.keys():
            next_square[num]=next_square[int(sqrt(num))]+1
    print(next_square)
    for k,v in next_square.items():
        print(k, v)
        if v>max:
            max = v
    return -1 if max==1 else max


# def streak(args, num, index):

#     if args[index]==num:
#         return 1+streak(args, num*num, index+1)


if __name__=='__main__':
    print(fun(int(x) for x in input().split(',')))