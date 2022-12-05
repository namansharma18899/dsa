# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def middle(head):
        #check next not being null
        fast = head.next
        slow = head
        while(fast):
            slow = slow.next
            if fast.next is not None:
                fast = fast.next.next
            else:
                break
        return slow

def fun(arr):
    arr = [int(x) for x in arr]
    temp_node = ListNode(arr[0])
    head = temp_node
    for index in range(1, len(arr)):
        temp_node.next = ListNode(arr[index])
        temp_node = temp_node.next
    return middle(head).val


if __name__=='__main__':
    tcs = int(input())
    while(tcs>0):
        print('res -> ',fun(input().split(' ')))
        tcs-=1