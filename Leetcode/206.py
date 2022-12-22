#from utils import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        curr = head
        prev=None
        temp = None
        # import pdb; pdb.set_trace()
        while(head is not None):
            head_next = head.next # 2 and beyond 
            head.next = prev # curr -> prev ... -> none
            prev = head
            head = head_next # 2 -> 3....
        return prev


    def reverseBetween(self, head, left, right):
        prev=None
        left_found=False
        result = head
        prev_node_at_reverse_begin=None
        head_next=None
        next_node_at_reverse_end=None
        node_reverse_begin=None
        # import pdb; pdb.set_trace()
        while(head is not None):
            if left_found:
                if head.val==right:
                    next_node_at_reverse_end = head.next # 5
                    head.next = prev # 4 -> 3 --> 2 -> None
                    # add nodes at begina and end 
                    prev_node_at_reverse_begin.next = head # 1 -> 4 -> 3 -> 2 -> None
                    node_reverse_begin.next = next_node_at_reverse_end
                    break
                else:
                    head_next = head.next # 2 and beyond 
                    head.next = prev # curr -> prev ... -> none
                    prev = head
                    head = head_next # 2 -> 3....
            elif head.val==left:
                prev_node_at_reverse_begin = prev #1
                node_reverse_begin = head
                left_found=True
                head_next = head.next #3
                head.next = prev# 2 -> None
                prev= head #prev -> 2
                head = head_next # 3 -> 4....
            else:
                prev = head
                head=head.next
        return result
            # head_next = head.next # 2 and beyond 
            # head.next = prev # curr -> prev ... -> none
            # prev = head
            # head = head_next # 2 -> 3....


def fun(args):
    sol = Solution()
    print(args)
    node = ListNode(args[0])
    head = node
    for index in range(1, len(args)):
        node.next = ListNode(val=args[index])
        node=node.next
    temp = head
    while(temp is not None):
        print('val -> ', temp.val)
        temp=temp.next
    res = sol.reverseBetween(head,2,4)
    while(res):
        print(res.val)
        res=res.next


if __name__=='__main__':
    print(fun([int(x) for x in input().split(',')]))