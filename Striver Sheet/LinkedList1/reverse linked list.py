class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverse(self, l1):
        pass

def fun(args):
    sol= Solution()
    args = [int(x) for x in args]
    head = ListNode(args[0])
    hn = head
    for index in range(1, len(args)):
        hn.next= ListNode(args[index])
    reversed_node = sol.reverse(head)
    


if __name__=='__main__':
    tcs = int(input())
    while(tcs>0):
        print('res -> ',fun(input().split(',')))
        tcs-=1