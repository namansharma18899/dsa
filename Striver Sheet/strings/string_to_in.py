class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if s=="":
            return 0
        sign = True
        res = 0
        def validate_output(res, sign):
            if not sign:
                res*=-1
            if res< (-2**31):
                return (-2**31)
            elif res > (2**31 -1):
                return (2**31 -1)
            return res
        if s[0]=='-' or s[0]=='+':
            if s[0]=='-':
                sign = False
            index = 1
        else:
            index = 0
        while(index < len(s) and s[index].isdigit()):
            each = s[index]
            res = res*10 + int(each)
            if res< (-2**31):
                break
            elif res > (2**31 -1):
                break
            index+=1
        return validate_output(res, sign)