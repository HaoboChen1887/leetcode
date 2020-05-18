# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#    def rightSideView(self, root: TreeNode) -> List[int]:
#        res = []
#        traverse(root, 0, res)
#        return res
#        
#
#def traverse(node, d, res):
#    if not node:
#        return
#    if d >= len(res):
#        res.append(node.val)
#    traverse(node.right, d + 1, res)
#    traverse(node.left, d + 1, res)
    
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        q, res = collections.deque([root]), []
        d = 0
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(curr.val)
            d += 1
        return res