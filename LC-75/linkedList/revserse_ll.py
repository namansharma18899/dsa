from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev= head
        while(head.next):
            curr = head.next
            if curr:
                head.next = curr.next
            curr.next = prev
            prev = curr
        head.next = None
        return prev




ob = Solution()
arr= [1,2,3,4,5]
head = ListNode(arr.pop(0))
temp = head
for each in arr:
    temp.next = ListNode(each)
    temp = temp.next

res = ob.reverseList(head)
while(res):
    print('node -> ', res.val)
    res = res.val
