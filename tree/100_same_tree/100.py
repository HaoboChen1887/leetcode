# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
#        stack1, stack2 = [p], [q]
#        res1, res2 = [], []
#        while stack1:
#            curr = stack1.pop()
#            res1.append(curr.val if curr else None)
#            if curr:
#                stack1.append(curr.left)
#                stack1.append(curr.right)
#                
#        while stack2:
#            curr = stack2.pop()
#            res2.append(curr.val if curr else None)
#            if curr:
#                stack2.append(curr.left)
#                stack2.append(curr.right)
#                
#        return res1 == res2

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        stack = [(p, q)]
        while stack:
            # DFS
            c_p, c_q = stack.pop()
            # BFS
            # c_p, c_q = stack.pop(0)
            if not c_p and not c_q:
                continue
            elif not c_p or not c_q:
                return False
            elif c_p.val != c_q.val:
                return False
            else:
                stack.append((c_p.left, c_q.left))
                stack.append((c_p.right, c_q.right))
        return True