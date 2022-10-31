import enum


def fun():
    nums = [8154,9139,8194,3346,5450,9190,133,8239,4606,8671,8412,6290] 
    # [0,0,0,0]
    # [10000]
    count = {}
    max = -1
    last_el = None
    for each in nums:
        if each%2==0:
            if each in count.keys():
                count[each]+=1
            else:
                count[each] = 1
            if count[each]>max:
                max = count[each]
                last_el = each
    res = -1
    print(last_el, max)
    for k,v in count.items():
        if v==max and k<=last_el:
            print(v, max, k, last_el)
            last_el = k
            res = k
    return res
print(fun())