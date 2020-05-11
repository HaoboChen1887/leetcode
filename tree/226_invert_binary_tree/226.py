# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#    def invertTree(self, root: TreeNode) -> TreeNode:
#        queue = [root]
#        while root and queue:
#            curr = queue.pop(0)
#            if not curr:
#                continue
#            else:
#                curr.left, curr.right = curr.right, curr.left
#                queue.append(curr.left)
#                queue.append(curr.right)
#        return root
    
    
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root