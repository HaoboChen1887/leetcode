# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(next=head)
        pre = dummy
        for _ in range(m - 1):
            pre = pre.next
        cur = pre.next
        for _ in range(m, n):
            t = cur.next
            cur.next = t.next
            t.next = pre.next
            pre.next = t
        return dummy.next