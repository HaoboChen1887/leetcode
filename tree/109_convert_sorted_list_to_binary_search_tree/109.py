# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#    def sortedListToBST(self, head: ListNode) -> TreeNode:
#        if not head:
#            return None
#        return helper(head, None)
#    
#    
#def helper(head, tail):
#    if head is tail:
#        return None
#    slow, fast = head, head
#    while fast is not tail and fast.next is not tail:
#        slow = slow.next
#        fast = fast.next.next
#        
#    node = TreeNode(slow.val)
#    node.left = helper(head, slow)
#    node.right = helper(slow.next, tail)
#    return node

    head = None
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        cnt, curr = 0, head
        self.head = head
        while curr:
            cnt += 1
            curr = curr.next
        return self.helper(0, cnt)
            
    def helper(self, low, high):
        if low >= high:
            return None
        print(low, high)
        mid = low + (high - low) // 2
        node = TreeNode(0)
        node.left = self.helper(low, mid)
        node.val = self.head.val
        self.head = self.head.next
        node.right = self.helper(mid + 1, high)
        return node