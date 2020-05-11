# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#    def preorderTraversal(self, root: TreeNode) -> List[int]:
#        if root is None:
#            return []
#        ans = [root.val]
#        ans += self.preorderTraversal(root.left)
#        ans += self.preorderTraversal(root.right)
#        return ans
    
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack, res = [root], []
        while stack:
            curr = stack.pop()
            if curr:
                res.append(curr.val)
                stack.append(curr.right)
                stack.append(curr.left)
        return res
        