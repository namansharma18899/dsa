from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return head
        result_pointer = head
        odd_pointer = head
        even_pointer = head.next
        index = 3
        while(even_pointer is not None):
            if index%2!=0:
                future_odd = even_pointer.next
                if not future_odd:
                    break
                future_even = future_odd.next
                even_start_pointer = odd_pointer.next
                odd_pointer.next = future_odd
                future_odd.next = even_start_pointer
                even_pointer.next = future_even
                # resetting Positional Pointers
                odd_pointer = future_odd
                even_pointer = future_even
            index+=1
        return result_pointer




ob = Solution()
arr= [1,2,3,4,5]
head = ListNode(arr.pop(0))
temp = head
for each in arr:
    temp.next = ListNode(each)
    temp = temp.next

res = ob.oddEvenList(head)
while(res):
    print('node -> ', res.val)
    res = res.val
