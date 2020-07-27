# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # use a counter to determine when to reverse the list
    # initialize counter to 1 so that reverse happens when i = k
    # in main function, pre is the tail of last group, cur is the current node
    # in reversek function, 
    #   pre is the tail of last group
    #   cur is the current node when reversing
    #   tail is the tail of the current group(the first node before reversing)
    # the way the reverse works is:
    #   connect tail to cur.next node (store the next node's info at the same time)
    #   connect curr node to the head node of the current group, which is pointed by pre
    #   connect pre to the new head, which is the current node
    #   move curr to the next node stored as tail.next
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 1:
            return head
        dummy = ListNode(-1, head)
        pre, cur = dummy, head
        i = 1
        while cur:
            if i % k == 0:
                pre = reversek(pre, cur.next)
                cur = pre.next
            else:
                cur = cur.next
            i += 1
        return dummy.next
            
def reversek(pre, nxt): 
    tail = pre.next
    cur = tail.next
    while cur is not nxt:
        tail.next = cur.next
        cur.next = pre.next
        pre.next = cur
        cur = tail.next
    return tail