#递归写法每个递归都有本地变量不需要另外维护，除了list是pass by reference

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#    def longestConsecutive(self, root: TreeNode) -> int:
#        res = 0
#        return findSeq(root, res, None)
#    
#def findSeq(node, res, par):
#    if not node:
#        return res
#    if not par or node.val != par.val + 1:
#        node.seq = 1
#    else:
#        node.seq = par.seq + 1
#    res = node.seq if node.seq > res else res
#    return max(findSeq(node.left, res, node), findSeq(node.right, res, node))
#            
#    def longestConsecutive(self, root: TreeNode) -> int:
#        if not root:
#            return 0
#        return findSeq(root, 0, root.val, 1)
#    
#def findSeq(node, res, prev, seq):
#    if not node:
#        return res
#    if node.val != prev + 1:
#        seq = 1
#    else:
#        seq += 1
#    res = max(seq, res)
#    return max(findSeq(node.left, res, node.val, seq), findSeq(node.right, res, node.val, seq))
            
    def longestConsecutive(self, root: TreeNode) -> int:
        res, q = 0, [[root, 1]]
        while root and q:
            curr, l = q.pop(0)
            res = max(l, res)
            for child in [curr.left, curr.right]:
                if child:
                    leng = l + 1 if child.val == curr.val + 1 else 1
                    q.append([child, leng])
        return res
                    
            
