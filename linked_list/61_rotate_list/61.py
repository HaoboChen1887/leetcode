# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # First find the length of the list
    # link the list together to form a cycle
    # starting from the head and move n - k % n steps
    # finally break the link
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        n = 1
        cur = head
        while cur.next:
            cur = cur.next
            n += 1
        
        cur.next = head
        cnt = 0
        while cnt < n - k % n:
            cur = cur.next
            cnt += 1
        res = cur.next
        cur.next = None
        return res
            
    
    # First find the length of the list
    # than take k % n to handle the case where k > n
    # use two pointer to find the position to break links and connect accordingly
#    def rotateRight(self, head: ListNode, k: int) -> ListNode:
#        if not head:
#            return head
#        length = 0
#        cnt = 0
#        dummy = ListNode(-1, head)
#        while head:
#            head = head.next
#            length += 1
#        slow, fast = dummy, dummy
#        while cnt < k % length and fast:
#            fast = fast.next
#            cnt += 1
#        
#        while fast.next:
#            slow = slow.next
#            fast = fast.next
#        
#        fast.next = dummy.next
#        dummy.next = slow.next
#        slow.next = None
#        return dummy.next