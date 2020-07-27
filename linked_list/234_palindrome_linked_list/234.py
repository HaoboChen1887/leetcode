# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
#    def isPalindrome(self, head: ListNode) -> bool:
#        if not head or not head.next:
#            return True
#        
#        slow, fast = head, head
#        st = []
#        while fast and fast.next:
#            slow = slow.next
#            fast = fast.next.next
#            
#        while slow:
#            st.append(slow)
#            slow = slow.next
#            
#        cur = head
#        while st:
#            if st.pop().val != cur.val:
#                return
#            cur = cur.next
#        return True

    # use two pointers to find the mid point of linked lists. 
    # During iterations, push the slow pointer on to a stack at the same time. 
    # When iterating through the second half, pop from the stack and compare.
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        
        slow, fast = head, head
        st = []
        while fast and fast.next:
            st.append(slow)
            slow = slow.next
            fast = fast.next.next
            
        if fast:
            slow = slow.next
        while st:
            if st.pop().val != slow.val:
                return False
            slow = slow.next
        return True
    
    # if space is limited to O(1), we can find the mid point 
    # and reverse the second half. Then compare the values of the two halves.