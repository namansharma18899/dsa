#from utils import *
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head, left, right):
        #Logic for reversing a linked list in O(1)
        previous_node = None
        curr = head
        # we need to store vars for positions
        # prvious before Reverse begins
        # Next node for the next linked list
        index = 1
        reverse_start_node = None
        reverse_start_prev_node, reverse_end_next_node = None, None
        while(head is not None):
            if index>=left and index<=right:
                if index==left:
                    # store the prevous in var & start reversing
                    reverse_start_prev_node=previous_node
                    temp_node = head.next
                    reverse_start_node=head
                    # previous_node=None # can cause NLP
                    head.next = previous_node
                    previous_node=head
                    head = temp_node
                elif index==right:
                    # store the next node from last...
                    reverse_end_next_node = head.next
                    head.next = previous_node
                    #Now we do the transfer -->
                    reverse_start_prev_node.next = head
                    reverse_start_node.next = reverse_end_next_node
                    return curr
                else:
                    temp_node = head.next
                    # previous_node=None # can cause NLP                    
                    head.next = previous_node
                    previous_node = head
                    head = temp_node
            else:
                previous_node=head #normal traversal nothing fancy
                head=head.next
            index+=1

def fun(args):
    node = ListNode(args.pop(0))
    head = node
    while(len(args)>0):
        node.next = ListNode(args.pop(0))
        node = node.next
    sol = Solution()
    return sol.reverseBetween(head, int(input()), int(input()))


if __name__=='__main__':
    print(fun(input().split(',')))