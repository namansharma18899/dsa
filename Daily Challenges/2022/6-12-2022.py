#https://leetcode.com/problems/odd-even-linked-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def fun(args):
    args = [int(x) for x in args]
    head = ListNode(args[0])
    temp = head
    for index in range(1, len(args)):
        head.next = ListNode(args[index])
        head = head.next
    res = solution(temp)
    while(res):
        print(res.val)
        res=res.next

def solution(head: ListNode):
    even = head.next
    odd = head.next.next
    print(even.val, odd.val)
    # import pdb; pdb.set_trace()
    r1 = odd
    r2 = even
    # if even or odd is None:
    #     return None
    while(even is not None and odd is not None):
        if head is None or head.next is None or head.next.next is None:
            return head
        even = head.next
        odd = head.next.next
        # print(even.val, odd.val)
        # import pdb; pdb.set_trace()
        r1 = odd
        r2 = even
        # if even or odd is None:
        #     return None
        while(even is not None and odd is not None):
            if odd.next is None:
                even.next=None
                odd.next = r2
                break
            temp_even = odd.next
            if temp_even.next is None:
                even.next=temp_even
                odd.next = r2
                break
            else:
                odd.next = temp_even.next
                even.next = temp_even
                even = even.next
                even.next = None
                odd = odd.next
            # print('even -> ', even.val, ' odd -> ', odd.val)
        head.next = r1
        return head
if __name__=='__main__':
    print(fun(input().split(' ')))