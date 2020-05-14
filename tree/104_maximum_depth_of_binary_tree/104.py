# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        q, res = [[root, 1]], 0
        while root and q:
            curr, d = q.pop(0)
            if not curr.left and not curr.right:
                res = max(d, res)
            for child in [curr.left, curr.right]:
                if child:
                    q.append([child, d + 1])
        return res
        

#    def maxDepth(self, root: TreeNode) -> int:
#        if not root:
#            return 0
#        if not root.left:
#            return 1 + self.maxDepth(root.right)
#        if not root.right:
#            return 1 + self.maxDepth(root.left)
#        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
         