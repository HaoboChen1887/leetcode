# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # first use two pointers to find the first node where they meet (except the head node)
    # then set one of the two pointers to head, move two pointers forward until they meet.
    # the node they meet is the entrance of the circle
    # This works because of the following reason
    # let a be the distance from head to the entrance
    # let b be the distace from entrance to where they first meet
    # let c be the length of the rest of the circle
    # the first time they meet
    # fast pointer has traveled a + b + c + b
    # slow pointer has traveled a + b
    # since fast pointer travels twice as fast as the slow pointer
    # we get 2 * (a + b) = a + b + c + b
    # and a = c
    # if we draw a picture we can see if fast pointer travels c and slow pointer travels a
    # the node they will meet is the entrance
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                break
        if not fast or not fast.next:
            return None
        slow = head
        while slow is not fast:
            slow = slow.next
            fast = fast.next
        return slow