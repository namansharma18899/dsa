def fun(args):
    args = [int(x) for x in args]
    k = int(input())
    previous_sum=0
    for index in range(0, k):
        previous_sum+=args[index]
    max = previous_sum
    print(previous_sum)
    for index in range(k, len(args)):
        previous_sum+=args[index]
        previous_sum-=args[index-k]
        print('prev -> ', previous_sum)
        if previous_sum > max:
            max = previous_sum

    return max


if __name__=='__main__':
    print(fun(input().split(' ')))