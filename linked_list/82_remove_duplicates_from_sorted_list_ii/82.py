# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(next=head)
        
        pre = dummy
        while pre.next:
            cur = pre.next
            while cur.next and cur.next.val == cur.val:
                cur = cur.next
            if cur is not pre.next:
                pre.next = cur.next
            else:
                pre = pre.next
        return dummy.next
