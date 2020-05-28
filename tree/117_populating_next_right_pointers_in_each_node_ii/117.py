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
        cur = dummy = Node(0, None, None, None)
        head = root
        while root:
            if root.left:
                # 每层第一次迭代时，相当于将dummy.next指向root.left
                # 对root的下一层进行联结
                cur.next = root.left 
                cur = cur.next 
            if root.right:
                # 每层第一次迭代时，相当于将dummy.next指向root.right
                # 对root的下一层进行联结
                cur.next = root.right 
                cur = cur.next
            root = root.next
            if not root:
                cur = dummy # 将cur重置为指向下一层第一个节点的节点
                root = dummy.next # root设为下一层第一个节点
                dummy.next = None # 断开连接防止联结下二层时在下一层进入死循环
        return head
         
        
#        helper(root)
#        return root
#        
#def helper(node):
#    if not node:
#        return None
#    p = node.next
#    while p:
#        if p.left:
#            p = p.left
#            break
#        if p.right:
#            p = p.right
#            break
#        p = p.next
#    if node.right:
#        node.right.next = p
#    if node.left:
#        node.left.next = node.right if node.right else p
#    # 此处必须先递归右边，因为右子树必须先被连接，不然上面的while没法找到正确的最左节点
#    helper(node.right)
#    helper(node.left)