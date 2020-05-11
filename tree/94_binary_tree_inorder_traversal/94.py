# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#    def inorderTraversal(self, root: TreeNode) -> List[int]:
#        if not root:
#            return []
#        ans = []
#        ans += self.inorderTraversal(root.left)
#        ans += [root.val]
#        ans += self.inorderTraversal(root.right)
#        return ans
#        
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack, res = [], []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res     