# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#    def minDepth(self, root: TreeNode) -> int:
#        if not root:
#            return 0
#        q, res = [[root, 1]], 0
#        while root and q:
#            curr, d = q.pop(0)
#            if not curr.left and not curr.right:
#                return d
#            for child in [curr.left, curr.right]:
#                if child:
#                    q.append([child, d + 1])
#        

    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        