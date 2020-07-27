# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        st = []
        dummy = ListNode(next=head)
        while head:
            st.append(head)
            head = head.next
        
        while st:
            cur = st.pop()
            cur.val += 1
            if cur.val > 9:
                cur.val = 0
                if not st:
                    dummy.next = ListNode(val=1, next=cur)
            else:
                break
        
        return dummy.next