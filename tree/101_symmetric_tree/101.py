# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#    def isSymmetric(self, root: TreeNode) -> bool:
#        if not root:
#            return True
#        stack = [(root.left, root.right)]
#        while stack:
#            c_p, c_q = stack.pop()
#            if not c_p and not c_q:
#                continue
#            elif not c_p or not c_q:
#                return False
#            elif c_p.val != c_q.val:
#                return False
#            else:
#                stack.append((c_p.left, c_q.right))
#                stack.append((c_p.right, c_q.left))
#        return True

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return isMirror(root.left, root.right)
    

def isMirror(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True
    elif not p or not q:
        return False
    elif p.val != q.val:
        return False
    else:
        return isMirror(p.left, q.right) and isMirror(p.right, q.left)