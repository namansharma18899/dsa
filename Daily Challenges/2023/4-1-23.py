from collections import Counter


class Solution:
    def minimumRounds(self, tasks):#: List[int]) -> int:
        kv = Counter(tasks)
        result = 0
        for k,v in kv.items():
            if v==1:
                return -1
            else:
                if v%3==0:
                    result+= int(v/3)
                else:
                    result+=int(v/3)+1
        return result

def fun(args):
    sol = Solution()
    return sol.minimumRounds([int(x) for x in args])


if __name__=='__main__':
    print(fun(input().split(',')))