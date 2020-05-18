# list operation in the front takes O(n) time
# Use collections.deque() to convert list to a deq object
# deq object has consistant time cost on both operations in the front and in the back

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
#        if not root:
#            return []
#        q, res = collections.deque([root]), []
#        rev = True
#        while q:
#            len_q = len(q)
#            level = collections.deque([])
#            for _ in range(len_q):
#                curr = q.popleft()
#                if rev:
#                    level.append(curr.val)
#                else:
#                    level.appendleft(curr.val)
#                if curr.left:
#                    q.append(curr.left)
#                if curr.right:
#                    q.append(curr.right)
#            rev = not rev
#            res.append(level)
#        return res
                
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = collections.deque([])
        dfs(root, 0, res)
        return res
        
def dfs(node, d, res):
    if not node:
        return
    if d >= len(res):
        res.append(collections.deque([]))
    if d % 2:
        res[d].appendleft(node.val)
    else:
        res[d].append(node.val)
    dfs(node.left, d + 1, res)
    dfs(node.right, d + 1, res)