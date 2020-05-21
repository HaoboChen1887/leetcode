# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class MyNode:
    def __init__(self, val):
        self.val = val
        self.cnt = 1
        self.left = None
        self.right = None
                    
class Solution:
#    def kthSmallest(self, root: TreeNode, k: int) -> int:
#        st, res = [], 0
#        while (st or root) and k > 0:
#            while root:
#                st.append(root)
#                root = root.left
#            root = st.pop()
#            k -= 1
#            res = root.val
#            root = root.right
#        return res

#    def kthSmallest(self, root: TreeNode, k: int) -> int:
#        cnt = count(root.left)
#        if k <= cnt:
#            return self.kthSmallest(root.left, k)
#        elif k > cnt + 1:
#            return self.kthSmallest(root.right, k - cnt - 1)
#        return root.val
#        
#def count(node):
#    if not node:
#        return 0
#    return 1 + count(node.left) + count(node.right)

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        node = build(root)
        return helper(node, k)
    
def build(node):
    if not node:
        return None
    my_node = MyNode(node.val)
    my_node.left = build(node.left)
    my_node.right = build(node.right)
    if my_node.left:
        my_node.cnt += my_node.left.cnt
    if my_node.right:
        my_node.cnt += my_node.right.cnt
    return my_node


def helper(node, k):
    if node.left:
        cnt = node.left.cnt
        if k <= cnt:
            return helper(node.left, k)
        elif k > cnt + 1:
            return helper(node.right, k - cnt - 1)
        return node.val
    else:
        if k == 1:
            return node.val
        return helper(node.right, k - 1)

