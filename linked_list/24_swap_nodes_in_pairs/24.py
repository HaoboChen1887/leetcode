# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        t = head.next
        head.next = self.swapPairs(head.next.next)
        t.next = head
        return t
    
#    def swapPairs(self, head: ListNode) -> ListNode:
#        dummy = ListNode(next=head)
#        pre = dummy
#        while pre.next and pre.next.next:
#            cur = pre.next.next
#            print(pre.val, cur.val)
#            pre.next.next = cur.next
#            cur.next = pre.next
#            pre.next = cur
#            pre = cur.next
#        return dummy.next