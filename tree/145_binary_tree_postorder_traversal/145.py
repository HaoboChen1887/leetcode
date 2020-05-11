# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#    def postorderTraversal(self, root: TreeNode) -> List[int]:
#        if not root:
#            return []
#        res = []
#        res += self.postorderTraversal(root.left)
#        res += self.postorderTraversal(root.right)
#        res += [root.val]
#        return res

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack, res = [root], []
        curr = root
        while stack and root:
            prev = curr
            curr = stack[-1]
            # when traversing to deeper layers
            if curr.left and curr.left != prev and curr.right != prev:
                stack.append(curr.left)
            elif curr.right and curr.right != prev:
                stack.append(curr.right)
            # going upward, a node can be added only when all of it's children are visited
            else:
                stack.pop()
                res.append(curr.val)
        return res
                
                