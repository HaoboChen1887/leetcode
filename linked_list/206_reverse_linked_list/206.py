# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        return helper(None, head)
        
def helper(prev, curr):
    if not curr:
        return prev
    nxt = curr.next
    curr.next = prev
    curr = helper(curr, nxt)
    return curr

#    def reverseList(self, head: ListNode) -> ListNode:
#        curr = head
#        prev = None
#        nxt = None
#        while curr:
#            nxt = curr.next
#            curr.next = prev
#            prev = curr
#            curr = nxt
#        return prev