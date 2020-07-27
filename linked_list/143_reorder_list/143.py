# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # find the mid point of the list
    # break the mid point link
    # reverse the second half of the list
    # alter between the two lists when inserting
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        cur = slow.next
        slow.next = None
        slow = cur
        
        pre = None
        while slow:
            cur = slow
            slow = slow.next
            cur.next = pre
            pre = cur
            
        first_half = True
        cur = head
        
        while cur and pre:
            nxt = cur.next
            cur.next = pre
            pre = pre.next
            cur.next.next = nxt
            cur = nxt
        
#        res = ListNode(-1, None)
#        while cur and pre:
#            if first_half:
#                res.next = cur
#                cur = cur.next
#            else:
#                res.next = pre
#                pre = pre.next
#            first_half = not first_half
#            res = res.next
#        res.next = pre if pre else cur
            
        
        # Another way of solving this problem is pushing all nodes onto a stack
        # and pop half of the stack(equivalent to reversing the second half of the linked list) 
        # and insert into the first half of the linked list.