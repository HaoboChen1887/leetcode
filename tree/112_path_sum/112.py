# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
#        if not root:
#            return False
#        return traverse(root, 0, sum)
#    
#def traverse(root, path_sum, sum):
#    print(path_sum)
#    if not root.left and not root.right:
#        path_sum += root.val
#        return path_sum == sum
#    path_sum += root.val
#    l = False
#    r = False
#    if root.left:
#        l =  traverse(root.left, path_sum, sum)
#    if root.right:
#        r =  traverse(root.right, path_sum, sum)
#    return l or r

#    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
#        if not root:
#            return False
#        if not root.left and not root.right:
#            return root.val == sum
#        sum -= root.val
#        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
    
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        stack = [root]
        
        while root and stack:
            curr = stack.pop()
            if not curr.left and not curr.right:
                if curr.val == sum:
                    return True
            if curr.left:
                curr.left.val += curr.val
                stack.append(curr.left)
            if curr.right:
                curr.right.val += curr.val
                stack.append(curr.right)
        return False