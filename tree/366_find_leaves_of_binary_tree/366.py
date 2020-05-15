# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#    def findLeaves(self, root: TreeNode) -> List[List[int]]:
#        if not root:
#            return []
#        res = []
#        dfs(root, res)
#        return res
#    
#def dfs(node, res):
#    if not node:
#        return -1
#    # 层数从上到下为降序（最深的leaf为0层）
#    depth = 1 + max(dfs(node.left, res), dfs(node.right, res))
#    if depth >= len(res):
#        res.append([])
#    res[depth].append(node.val)
#    return depth

    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        res = []
        while root:
            leaves = []
            root = remove(root, leaves)
            res.append(leaves)
        return res
        
def remove(node, leaves):
    if not node:
        return None
    if not node.left and not node.right:
        leaves.append(node.val)
        return None
    node.left = remove(node.left, leaves)
    node.right = remove(node.right, leaves)
    return node