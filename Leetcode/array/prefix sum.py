def fun(args):
    args = [int(x) for x in args]
    previous_sum = [args[0]]
    for index in range(0,len(args)):
        previous_sum.append(previous_sum[-1]+args[index])
    inp = [int(x) for x in input().split(' ')]
    return previous_sum[inp[1]]-previous_sum[inp[0]]+args[inp[1]]

if __name__=='__main__':
    print(fun(input().split(' ')))