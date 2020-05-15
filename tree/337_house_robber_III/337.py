# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#    def rob(self, root: TreeNode) -> int:
#        m = {}
#        return helper(root, m)
#        
#def helper(node, m):
#    if not node:
#        return 0
#    if node in m:
#        return m[node]
#    val = 0
#    
#    # combination that doesn't include immediate children
#    if node.left:
#        val += helper(node.left.left, m) + helper(node.left.right, m)
#    if node.right:
#        val += helper(node.right.left, m) + helper(node.right.right, m)
#    val += node.val
#    
#    # take the maximum with combiniation that includes immediate children
#	 # at this point, val is the optimal solution for this subtree
#    val = max(val, helper(node.left, m) + helper(node.right, m))
#    
#    m[node] = val
#    
#    return val


    def rob(self, root: TreeNode) -> int:
        res = [0, 0]
        res = helper(root)
        return max(res)
    
def helper(node):
    if not node:
        return 0, 0
    l_res = helper(node.left)
    r_res = helper(node.right)
    # res0 is the optimal solution for the subtree not including current node
    # res1 is the optimal solution for the subtree including current node
    return [max(l_res) + max(r_res), node.val + l_res[0] + r_res[0]]
