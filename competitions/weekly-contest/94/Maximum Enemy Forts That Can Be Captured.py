#from utils import *
class Solution:
    def captureForts(self, forts) -> int:
        stack = []
        max_forts = -99
        left_forts = [None]*len(forts)
        right_forts = [None]*len(forts)
        count = None
        for index in range(0, len(forts)):
            if forts[index]==1:
                count = 0
            else:
                if forts[index]==-1:
                    left_forts[index]=count if count is not None else 0
                    count = None
                else:
                    if count is not None:
                        count+=1
        for index in range(len(forts)-1,-1,-1):
            if forts[index]==1:
                count = 0
            else:
                if forts[index]==-1:
                    right_forts[index]=count if count is not None else 0
                    count = None
                else:
                    if count is not None:
                        count+=1
            print(count)
        for index in range(0, len(forts)):
            print(left_forts[index], right_forts[index])
            if forts[index]==-1:
                temp = max(left_forts[index],right_forts[index])
                if temp>max_forts:
                    max_forts=temp
        return max_forts
        # for index in range(0, len(forts)):
        #     if forts[index]!=0:
        #         count = 0
        #         while(len(stack)> 0):
        #             el = stack.pop()
        #             if el==0:
        #                 count+=1
        #             else:
        #                 if count>max_forts:
        #                     max_forts=count
        #                 break
        #         stack.append(forts[index])
        #     else:
        #         stack.append(0)
        return max_forts

def fun(args):
    sol = Solution()
    return sol.captureForts(forts=args)


if __name__=='__main__':
    print(fun([int(x) for x in input().split(',')]))