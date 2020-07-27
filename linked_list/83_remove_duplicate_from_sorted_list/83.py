# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        head.next = self.deleteDuplicates(head.next)
        res = head if head.val != head.next.val else head.next
        return res
    
#    def deleteDuplicates(self, head: ListNode) -> ListNode:
#        if not head or not head.next:
#            return head
#        
#        cur = head
#        while cur and cur.next:
#            if cur.val == cur.next.val:
#                cur.next = cur.next.next
#            else:
#                cur = cur.next
#        return head
    
#    def deleteDuplicates(self, head: ListNode) -> ListNode:
#        if not head or not head.next:
#            return head
#        
#        slow, fast = head, head.next 
#        while fast:
#            while fast and fast.val == slow.val:
#                fast = fast.next
#            slow.next = fast
#            slow = fast
#            
#        return head