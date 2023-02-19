class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        a=a[::-1]
        b=b[::-1]
        carry = 0
        mx = max(len(a),len(b))
        for index in range(mx):#,-1,-1):
            aind= a[index] if index<len(a) else '0'
            bind = b[index] if index<len(b) else '0'
            if aind==bind:
                if aind=='1':
                    if carry=='1':
                        res.append(1)
                        carry='1'
                    else:
                        res.append(0)
                        carry='1'
                else:
                    if carry=='1':
                        res.append(1)
                        carry='0'
                    else:
                        res.append(0)
            else:
                if carry=='1':
                    res.append(0)
                    carry='1'
                else:
                    res.append(1)
        if carry=='1':
            res.append(1)
        rs = ""
        for each in res[::-1]:
            rs+=str(each)
        return rs

def fun(args):
    sol= Solution()
    return sol.addBinary(input(),input())


if __name__=='__main__':
    tcs = int(input())
    while(tcs>0):
        print('res -> ',fun(None))#input().split(',')))
        tcs-=1