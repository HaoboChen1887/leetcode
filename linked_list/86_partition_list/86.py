# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # find the node before first node >= x, need a dummy node to deal with when head node is >= x
    # insert to the front of the first node >= x if found any node < x
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(-1, head)
        s_tail, l_tail = dummy, dummy
        while s_tail.next and s_tail.next.val < x:
            s_tail = s_tail.next
            
        l_tail = s_tail.next
        if not l_tail:
            return dummy.next
        cur = l_tail
        
        while cur:
            if cur.val < x:
                nxt = cur.next
                cur.next = s_tail.next
                s_tail.next = cur
                l_tail.next = nxt
                s_tail = cur
                cur = nxt
            else:
                l_tail = cur
                cur = cur.next
        return dummy.next
    
    # Alternative method: pull out all nodes >= k to a new list and 
    # attach the new list to the remainder of the original list
                
                