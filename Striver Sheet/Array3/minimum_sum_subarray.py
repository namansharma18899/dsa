def min_sum():
    arr = [-7,3,4,-2,-3,1,-3]
    res = arr[0]
    s_sum = 0
    for index, val in enumerate(arr):
        if s_sum+val < val:
            s_sum+=val
        else:
            s_sum=val
        res = min(res, s_sum)
    return res
    

print(min_sum())

    