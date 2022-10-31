def fun():
    height = [1,8,6,2,5,4,8,3,7]
    lmax, rmax = [1]*len(height), [1]*len(height)
    max = height[0]
    for index in range(1, len(height)):
        lmax[index] = max
        if height[index] > max:
            max = height[index]
    max = height[len(height)-1]
    max_index = len(height)-1
    for index in range(len(height)-1, -1 ,-1):
        rmax[index] = max
        if height[index] > max:
            max = height[index]
    sum =0
    print(lmax)
    print(rmax)
    brd = 0
    max = 0
    for index in range(1, len(height)-1):
        if height[index]<min(lmax[index], rmax[index]):
            sum+=min(lmax[index], rmax[index])
    return sum


print(fun())