def fun(nums):
    nums = [int(each) for each in nums]
    arr1 = nums[0 : int(len(nums) / 2)]
    arr2 = nums[int(len(nums) / 2) : len(nums)]
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)
    print(arr1, arr2)
    operations = 0
    p1, p2 = 0, 0
    for each in arr1:
        p1 += each
    for each in arr2:
        p2 += each
    print(p1, p2)
    # import pdb; pdb.set_trace()
    return False


if __name__ == "__main__":
    print(fun(input().split(",")))
