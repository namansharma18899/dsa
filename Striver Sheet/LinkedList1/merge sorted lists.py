from Leetcode.utils.utility import ListNode, create_linked_list_from_array

class Solution:
    def merge(self,l1,l2):
        p1 = l1
        p2 = l2
        prev = None
        head = None
        while(p1!=None and p2!=None):
            if p1.val <= p2.val: # BASIC MERGE SORT LOGIC
                if prev:
                    prev.next=p1
                    prev=prev.next
                else:
                    prev = ListNode(p1.val)
                    head = prev
                p1=p1.next
            else:
                if prev:
                    prev.next=p2
                    prev=prev.next
                else:
                    prev = ListNode(p2.val)
                    head = prev
                p2=p2.next
        if p1==None and p2!=None:
            prev.next=p2
        elif p2==None and p1!=None:
            prev.next=p1
        return head

        #

def fun(args):
    sol= Solution()
    args = [int(x) for x in args]
    args2 = [int(x) for x in input().split(',')]
    head = create_linked_list_from_array(args)
    head2 = create_linked_list_from_array(args2)
    res = sol.merge(head,head2)
    return res


if __name__=='__main__':
    tcs = int(input())
    while(tcs>0):
        print('res -> ',fun(input().split(',')))
        tcs-=1