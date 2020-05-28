# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = collections.deque([(0, root)])
        m = collections.defaultdict(list)
        res = []
        while q:
            idx, curr = q.popleft()
            m[idx].append(curr.val)
            if curr.left:
                q.append((idx-1, curr.left))
            if curr.right:
                q.append((idx+1, curr.right))
        for key in sorted(m):
            res.append(m[key])
        return res
        