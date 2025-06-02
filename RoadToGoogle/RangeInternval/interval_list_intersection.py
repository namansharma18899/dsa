def overlap(fl, sl, i , j):
    def get_se(sa, ea, sb, eb):
        if sa > eb:
            return None, None
        end, start= eb, None
        if ea==sb:
            start = end
        elif sa <= sb:
            start = sb
        else:
            start = sa
        return start, end

    sa, ea= fl[i][0], fl[i][1]
    sb, eb = sl[j][0], sl[j][1]

    # edge case
    if ea >= eb:
        start, end = get_se(sa,ea,sb,eb) 
    else:
        start, end = get_se(sb,eb, sa, ea) 
    if start is not None and end is not None:
        return [start, end]
    return None




testcases = [\
    {'a': [[0,2],[5,10],[13,23],[24,25]], 'b':[[1,5],[8,12],[15,24],[25,26]], 'res': [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]},
    {'a':[[1,5],[8,12],[15,24],[25,26]],'b':[[0,2],[5,10],[13,23],[24,25]], 'res': [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]},
    {'a': [[1,3],[5,9]], 'b':[], 'res': []},
    {'a': [], 'b':[[1,3],[5,9]], 'res': []},
    {'a': [[1,199]], 'b':[[1,5],[8,12],[15,24],[25,26]], 'res':[[1,5],[8,12],[15,24],[25,26]]},
    {'a': [[1,5],[8,12],[15,24],[25,26]], 'res':[[1,5],[8,12],[15,24],[25,26]], 'b':[[1,199]]}
    ]


for index, each in enumerate(testcases):
    a,b = each['a'], each['b']
    i, j = 0,0
    result = []
    while(i < len(a) and j<len(b)):
        olp = overlap(a,b,i,j)
        if olp is not None:
            result.append(olp)
        if a[i][1] > b[j][1]:
            j+=1 
        else:
            i+=1
    print('PASSED ' if each['res'] == result else f'FAILED a:{a} b:{b} \n Assertion: {each["res"]} \t result: {result}')