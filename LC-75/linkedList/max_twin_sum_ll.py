from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middle(self, head):
        #check next not being null
        fast = head.next
        slow = head
        while(fast):
            if fast.next is not None:
                fast = fast.next.next
            else:
                break
            slow = slow.next
        return slow
    
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

    def pairSum(self, head: Optional[ListNode]) -> int:
        mid = self.middle(head)
        print('mid -> ', mid.val)
        first = mid.next
        mid.next = None
        reversed = self.reverseList(first)
        print('rev -> ', reversed.val)
        res = 0
        while(head):
            res = max(res, head.val + reversed.val)
            head=head.next
            reversed = reversed.next
        return res



ob = Solution()
arr= [5,4,2,1]
head = ListNode(arr.pop(0))
temp = head
for each in arr:
    temp.next = ListNode(each)
    temp = temp.next

print(ob.pairSum(head))
# while(res):
#     print('node -> ', res.val)
#     res = res.val
