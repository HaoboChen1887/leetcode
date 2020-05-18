# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
#    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#        if not root:
#            return None
#        if root.val > p.val and root.val > q.val:
#            return self.lowestCommonAncestor(root.left, p, q)
#        elif root.val < p.val and root.val < q.val:
#            return self.lowestCommonAncestor(root.right, p, q)
#        else:
#            return root

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        st, res = [root], None
        while st:
            if root.val < min(p.val, q.val):
                root = root.right
            elif root.val > max(p.val, q.val):
                root = root.left
            else:
                return root
        return None