# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
#        if not root:
#            return []
#        q, res = [root], []
#        while q:
#            q_len = len(q)
#            lvl = []
#            for _ in range(q_len):
#                curr = q.pop(0)
#                lvl.append(curr.val)
#                if curr.left:
#                    q.append(curr.left)
#                if curr.right:
#                    q.append(curr.right)
#            res.insert(0, lvl)
#        return res
    
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        traverse(root, 0, res)
        return reversed(res)
        
def traverse(node, d, res) -> List[List[int]]:
    if not node:
        return
    if d >= len(res):
        res.append([])
    res[d].append(node.val)
    traverse(node.left, d + 1, res)
    traverse(node.right, d + 1, res)