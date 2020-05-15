# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = -sys.maxsize
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxPath(root)
        return self.res
        
    # recursive function returns the longest possible path 
    # starting from a leaf and terminate at current node
    # res records the longest global path
    def maxPath(self, node):
            if not node:
                return 0
            left = max(self.maxPath(node.left), 0)
            right = max(self.maxPath(node.right), 0)
            self.res = max(self.res, left + right + node.val)
            return max(left, right) + node.val