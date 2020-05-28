"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        start = root
        while start.left:
            curr = start
            while curr:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                curr = curr.next
            start = start.left
        return root
    
#    def connect(self, root: 'Node') -> 'Node':
#        helper(root)
#        return root
#    
#def helper(node):
#    if not node:
#        return
#    if node.left:
#        node.left.next = node.right
#    if node.right:
#        if node.next:
#            node.right.next = node.next.left
#    helper(node.left)
#    helper(node.right)
