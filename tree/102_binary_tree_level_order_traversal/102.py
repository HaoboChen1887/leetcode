# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        stack, res = [root], []
        while root and stack:
            res.append([node.val for node in stack])
            next_layer = []
            for curr in stack:
                if curr.left:
                    next_layer.append(curr.left)
                if curr.right:
                    next_layer.append(curr.right)    
            stack = next_layer
        return res