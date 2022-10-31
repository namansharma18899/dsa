def fun(mat):
    k= int(input())
    mat =[[1,0,0,0],
    [1,1,1,1],
    [1,0,0,0],
    [1,0,0,0]]
    res = []
    for index, row in enumerate(mat):
        count=0
        print(row)
        for col in row:
            if col==0:
                break
            else:
                count+=1
        res.append([index, count])
    # print(res)
    return [val[0] for index,val in enumerate(sorted(res, key=lambda x: x[1])) if index<k]
    # return 


if __name__=='__main__':
    print(fun(input().split(',')))