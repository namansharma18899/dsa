def fun(args):
    nums = [int(x) for x in args]
    increasing_monotone = None
    for index in range(1, len(nums)):
        print('index -> ', increasing_monotone)
        if nums[index]==nums[index-1]:
            continue
        if increasing_monotone is not None:
            if increasing_monotone==True:
                if nums[index]<nums[index-1]:
                    return False
            elif nums[index]>nums[index-1]:
                return False
        else:
            if nums[index]>nums[index-1]:
                increasing_monotone=True
            else:
                increasing_monotone=False
    return True


if __name__=='__main__':
    print(fun(input().split(',')))