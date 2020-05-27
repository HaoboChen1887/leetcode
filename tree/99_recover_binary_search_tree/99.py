# Morris inorder traversal
# 循环至当前节点为空
#     如果当前节点左孩子为空，则输出当前节点并将其右孩子作为当前节点
#     如果当前节点左孩子不为空
#         在当前节点的左子树中找到当前节点在中序遍历中的前驱节点
#         如果前驱节点的右孩子为空
#             将它的右孩子设为当前节点
#             当前节点更新为当前节点的左孩子
#         如果前驱节点的右孩子为当前节点
#             将它的右孩子设为空（恢复树的形状）
#             输出当前节点
#             当前节点更新为当前节点的右孩子

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur = root
        pre, p, first, second = [None] * 4
        while cur:
            if cur.left:
                p = cur.left
                while p.right and p.right is not cur:
                    p = p.right
                if p.right is cur:
                    p.right = None
                else:
                    p.right = cur
                    cur = cur.left
                    continue
            if pre and pre.val > cur.val:
                if not first:
                    first = pre
                second = cur
            pre = cur
            cur = cur.right
                

        first.val, second.val = second.val, first.val