# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        #basic approach whicih comes to mind
        sum = None
        head = sum
        carry= 0
        while(l1 or l2):
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            if not sum:
                sum = ListNode(int((v1+v2)%10))
                head = sum
                if (v1+v2)>9:
                    carry=1
            else:
                sum.next = ListNode(int((v1+v2+carry)%10))
                carry = 1 if (v1 + v2 + carry) > 9 else 0
                sum = sum.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        sum.next = ListNode(1) if carry==1 else None
        return head
            

def fun(args):
    sol= Solution()
    return sol.fname(args)


if __name__=='__main__':
    tcs = int(input())
    while(tcs>0):
        print('res -> ',fun(input().split(',')))
        tcs-=1
