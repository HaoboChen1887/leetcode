# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or p is root or q is root:
            return root
        l = self.lowestCommonAncestor(root.left, p, q)
        # 如果l存在并且不是pq那l一定是LCA不存在pq在右边的情况
        if l and l is not p and l is not q:
            return l
        r = self.lowestCommonAncestor(root.right, p, q)
        # 如果lr都存在说明pq分别在当前节点的两边，此时当前节点就是LCA 
        if l and r:
            return root
        # 如果只有l说明pq都在当前节点的左边
        # 此时有两种情况
        # 1.qp中的一个为LCA，此时会返回qp中位置较高的一个
        # 2.返回qp的LCA
        elif l:
            return l
        else:
            return r