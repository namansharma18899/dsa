from typing import Optional
from Leetcode.utils.utility import ListNode, create_linked_list_from_array

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #2 pointers
        slow = head
        fast = head.next
        while(fast):
            slow=slow.next
            if fast.next:
                fast = fast.next.next
            else:
                return slow
        return slow

def fun(args):
    sol= Solution()
    args = [int(x) for x in args]
    head = create_linked_list_from_array(args)
    obj = sol.middleNode(head)
    print(type(obj), obj)
    # return sol.fname(args)


if __name__=='__main__':
    tcs = int(input())
    while(tcs>0):
        # print('res -> ',
        fun(input().split(','))
        tcs-=1