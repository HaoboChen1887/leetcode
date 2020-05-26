# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        a = root.val
        root = root.right if target > root.val else root.left
        if not root:
            return a
        b = self.closestValue(root, target)
        if abs(a - target) > abs(b - target):
            return b
        else:
            return a
        
        
#    def closestValue(self, root: TreeNode, target: float) -> int:
#        min_diff = sys.maxsize
#        res = root
#        while root:
#            diff = abs(target - root.val)
#            min_diff = min(diff, min_diff)
#            res = res if min_diff < diff else root
#            if target == root.val:
#                return root.val
#            elif target > root.val:
#                root = root.right
#            else:
#                root = root.left
#        return res.val