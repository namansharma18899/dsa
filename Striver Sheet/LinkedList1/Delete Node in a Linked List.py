# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        p=None
        while(node.next!=None):
            node.val = node.next.val
            if node.next.next==None:
                p=node
            node=node.next
        p.next = None
        

def fun(args):
    sol= Solution()
    return sol.fname(args)


if __name__=='__main__':
    tcs = int(input())
    while(tcs>0):
        print('res -> ',fun(input().split(',')))
        tcs-=1