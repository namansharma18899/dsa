def fun(args):
    args = [int(x) for x in args]
    prev = [args[0]]
    sum = int(input())
    for index in range(1, len(args)):
        prev.append(prev[-1]+args[index])
        if prev[-1]==sum:
            return True
        elif prev[-1]>sum:
            try:
                prev.index(prev[-1]-sum)
                return True
            except Exception as e:
                return False


if __name__=='__main__':
    print(fun(input().split(' ')))