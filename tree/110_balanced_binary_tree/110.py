# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        d, isb = DFS(root, 1)
        
def DFS(root, d):
    if not root:
        return 0
    if not root.left and not root.right:
        return 0
    
    dl, isbl = DFS(root.left, d + 1)
    dr, isbr = DFS(root.right, d + 1)
    return max(dl, dr) abs(dl - dr) <= 1, isbl and isbr
        