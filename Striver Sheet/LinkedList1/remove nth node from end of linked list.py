# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # iterate all, save last nth nodes -> iterate to nth -> remove nth
        # reverse the linked list -> remvoe nth
        # 2 pointers
        if head.next==None:
            return None
        slow  = head
        hd= head
        fast = head
        for index in range(0, n-1):
            fast = fast.next
        prev = None
        while(fast.next):
            prev = slow
            slow=slow.next
            fast=fast.next
        if prev==None:
            temp = hd.next
            hd.next = None
            return temp
        prev.next  = slow.next
        return hd


def fun(args):
    sol= Solution()
    return sol.fname(args)


if __name__=='__main__':
    tcs = int(input())
    while(tcs>0):
        print('res -> ',fun(input().split(',')))
        tcs-=1