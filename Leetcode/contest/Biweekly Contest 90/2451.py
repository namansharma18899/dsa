from collections import defaultdict
from string import ascii_lowercase

def most_frequent(List):
    return max(set(List), key = List.count)

def fun(args):
    # [1] as stated in the problem, there will be two groups 
        #     of words according to their difference array;
        #     we'll store them in a hashmap/dict using the
        #     difference array as a key
    eq = defaultdict(list)
    print(eq)
    for w in args:
        # [2] in Python, keys are immutable, thus we convert
        #     the difference array to 'tuple'
        diff = [ord(a)-ord(b) for a, b in zip(w[:-1], w[1:])]
        eq[tuple(diff)].append(w)
    print(eq)
    # [3] as guaranteed in the problem, there will be 2
    #     groups of words, one of them of size 1
    for _, ws in eq.items():
        if len(ws) == 1:
            return ws[0]

    # alphs = {}
    # index=0
    # for c in ascii_lowercase:
    #     alphs[c]=index
    #     index+=1
    # res = {}
    # print(alphs)
    # # import pdb; pdb.set_trace()
    # for each in args:
    #     temp = []
    #     for index in range(1,len(each)):
    #             temp.append(alphs[each[index]]-alphs[each[index-1]])
    #     res[each]=temp
    # for k,v in res.items():
    #     if v!=coun:
    #         return k
    # return res
if __name__=='__main__':
    print(fun(input().split(',')))