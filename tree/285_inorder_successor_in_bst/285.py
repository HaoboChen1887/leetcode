# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root.val <= p.val:
            return self.inorderSuccessor(root.right, p)
        else:
            left = self.inorderSuccessor(root.left, p)
            if left:
                return left
            return root
    
#    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
#        res = None
#        while root:
#            if root.val > p.val:
#                res = root
#                root = root.left
#            else:
#                root = root.right
#        return res
    
#    pre, suc = None, None
#    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
#        if not p:
#            return None
#        self.helper(root, p)
#        return self.suc
#    
#    def helper(self, node, p):
#        if not node:
#            return
#        self.helper(node.left, p)
#        if p == self.pre:
#            self.suc = node
#        self.pre = node
#        self.helper(node.right, p)
    
#    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
#        st, pre = [], None
#        while st or root:
#            while root:
#                st.append(root)
#                root = root.left
#            root = st.pop()
#            if pre == p:
#                return root
#            pre = root
#            root = root.right
#        return None
        
