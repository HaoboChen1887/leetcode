# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#    res = 0
#    def countUnivalSubtrees(self, root: TreeNode) -> int:
#        if not root:
#            return 0
#        self.dfs(root)
#        return self.res
#        
#    def dfs(self, node):
#        if not node.left and not node.right:
#            self.res += 1
#            return True
#        uni = True
#        if node.left:
#            uni = node.val == node.left.val and uni
#            uni = self.dfs(node.left) and uni
#        if node.right:
#            uni = node.val == node.right.val and uni
#            uni = self.dfs(node.right) and uni
#            
#        if uni:
#            self.res += 1
#        return uni
#    

        
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if not root:
            return 0
        s, res = [root], []
        child = root
        while root and s:
            curr = s[-1]
            # pop only when curr is leaf node or when iterating upwards
            if not curr.left and not curr.right or\
               curr.left == child or curr.right == child:
                    if not curr.left and not curr.right:
                        res.append(curr)
                    elif not curr.left and curr.right in res and curr.val == curr.right.val:
                        res.append(curr)
                    elif not curr.right and curr.left in res and curr.val == curr.left.val:
                        res.append(curr)
                    elif curr.left in res and curr.right in res and curr.val == curr.right.val == curr.left.val:
                        res.append(curr)
                    s.pop();
                    child = curr
            else:
                if curr.right: 
                    s.append(curr.right)
                if curr.left:
                    s.append(curr.left)
                    
        return len(res)