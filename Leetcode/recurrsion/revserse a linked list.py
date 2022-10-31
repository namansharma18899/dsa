# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        # if head.next==None:
        #     return head
        # temp=self.reverseList(head.next)
        # head.next = None
        # while(tm.next!=None):
        #     tm=tm.next
        # tm.next=head
        # # temp.next=head
        # print('tmp -> ', temp, ' --nxt -', temp.next)
        # return temp
        return self.recur(head, None)
    def recur(self, head, res):
        if res==None:
            res=ListNode(val=head.val)
        else:
            temp = res
            while(True):
                if temp.next==None:
                    temp.next=head
                    break
                temp=temp.next
        if (head.next==None):
            return head
        else:
            return self.recur(head.next, res)

def fun(args):
    x = Solution()
    head = None
    for index,val in enumerate(args):
        if index==0:
            head = ListNode(val=val)
            ln = head
        else:
            ln.next=ListNode(val=val)
        print('ln ->', ln.val,ln.next.val if ln.next is not None else ln.next)
    print(x.reverseList(head))
    # return args


if __name__=='__main__':
    print(fun(input().split(',')))