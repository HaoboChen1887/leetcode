# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#    def isValidBST(self, root: TreeNode) -> bool:
#        st = []
#        prev = None
#        while st or root:
#            while root:
#                st.append(root)
#                root = root.left
#            root = st.pop()
#            if prev:
#                print(prev.val, root.val)
#            if prev and prev.val >= root.val:
#                return False
#            prev = root
#            root = root.right
#        return True
    prev = -sys.maxsize
    def isValidBST(self, root: TreeNode) -> bool:
        return self.traverse(root)
    
    
    def traverse(self, node) -> bool:
        if not node:
            return True
        res = self.traverse(node.left) self.prev < node.val
        self.prev = node.val
        res = self.traverse(node.right) and res
        return res