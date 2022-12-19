#from utils import *
# from ../Leetcode/ut/ils import *
# from  ../Leetcode/utils/utility.py import is_number


class Solution:
    def is_number(self,n):
        is_number = True
        try:
            num = float(n)
            # check for "nan" floats
            is_number = num == num   # or use `math.isnan(num)`
        except ValueError:
            is_number = False
        return is_number
    def operation(self, num1, num2, op):
        # operaitions = {"+":+,"/":/,"-":-,"*":*}
        if op=="+":
            return int(num1+num2)
        elif op=="-":
            return int(num1-num2)
        elif op=="*":
            return int(num1*num2)
        elif op=="/":
            return int(num1/num2)

    def evalRPN(self, tokens) -> int:
        stack = list()
        for index in range(0,len(tokens)):
            if self.is_number(tokens[index]):
                stack.append(int(tokens[index]))
            else:
                num2=stack.pop()
                num1=stack.pop()
                res = self.operation(num1,num2,tokens[index])
                stack.append(res)
        return stack.pop()

stack
num1=stack.pop()
num2=stack.pop()
if val=="+":
    stack.append(int(num2+num2))
elif val=="-":
    stack.append(int(num2-num2))
elif val=="*":
    stack.append(int(num2*num2))
elif val=="/":
    stack.append(int(num2/num2))


def fun(args):
    sol = Solution()
    return sol.evalRPN(args)
    # return args


if __name__=='__main__':
    print(fun(input().split(',')))

#10,6,9,3,+,-11,*,/,*,17,+,5,+