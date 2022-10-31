def fun(seq_a, seq_b,n):
    sunion = set(seq_a).union(set(seq_b))
    sint = set(seq_a).intersection(set(seq_b))
    count = 0
    for x in range(1, n+1):
        if x not in sunion:
            count+=1
    return len(set(seq_a).intersection(set(seq_b))), count


if __name__=='__main__':
    # testcase = open('./testcase.txt', 'r')
    # results = open('./results.txt','r')
    # TesetCases = testcase.readlines()
    # Results = results.readlines()
    # count, mul = 0,int(TesetCases[0])
    # print(count, mul)
    # for index in range(1, len(TesetCases), mul):
    #     line= TesetCases[index]
    #     inp = line.split(' ')
    #     n,m,k = int(inp[0]),int(inp[1]),int(inp[2])
    #     seq_a=[int(x) for x in TesetCases[index+1].split(' ')]
    #     seq_b=[int(x) for x in TesetCases[index+2].split(' ')]
    #     res = fun(seq_a, seq_b, n)
    #     expected = Results[count].split('|')[1]
    #     count+=1
    #     try:
    #         assert str(res) == str(expected)
    #     except Exception as e:
    #         print(type(e))
    #         print(f'FAILED {res}, expected {expected}')
    #     count+=1
    #     print(f'Passed {res}, expected {expected}')
    tcs = int(input())
    while(tcs > 0):
        inp = input().split(' ')
        n,m,k = int(inp[0]),int(inp[1]),int(inp[2])
        seq_a =[int(x) for x in input().split(' ')] #ignored
        seq_b =[int(x) for x in input().split(' ')] #tracked
        res = fun(seq_a, seq_b, n)
        print(res[0],' ',res[1])
        tcs-=1