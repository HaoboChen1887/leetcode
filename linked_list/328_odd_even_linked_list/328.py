# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        odd, even, even_head = head, head.next, head.next
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head
        
#    def oddEvenList(self, head: ListNode) -> ListNode:
#        if not head or not head.next:
#            return head
#        odd, even = head, head.next
#        while even and even.next:
#            t = odd.next
#            odd.next = even.next
#            even.next = even.next.next
#            odd.next.next = t
#            odd = odd.next
#            even = even.next
#        return head