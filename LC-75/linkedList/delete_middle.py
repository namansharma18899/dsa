# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = slow
        prev = None
        while(fast is not None):
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                break
            prev = slow
            slow = slow.next
        prev.next = slow.next # deleting
        return slow


ob = Solution()
arr= [1,2,3,4,5]
head = ListNode(arr.pop())
temp = head
for each in arr:
    temp.next = ListNode(each)
    temp = temp.next

res = ob.deleteMiddle(head)
while(res):
    print('node -> ', res.val)
    res = res.val
