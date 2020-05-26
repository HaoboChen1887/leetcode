# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
#    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
#        st, res = [], []
#        while root or st:
#            while root:
#                st.append(root)
#                root = root.left
#            root = st.pop()
#            if k > len(res) or -abs(target - root.val) > heapq.nsmallest(1, res)[0][0]:
#                print("add")
#                if k <= len(res):
#                    heapq.heappushpop(res, (-abs(root.val - target), root.val))
#                else:
#                    heapq.heappush(res, (-abs(root.val - target), root.val))
#            root = root.right
#            
#        return [i[1] for i in res]

    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        st, res = [], collections.deque([])
        while root or st:
            while root:
                st.append(root)
                root = root.left
            root = st.pop()
            if k > len(res):
                res.append(root.val)
            elif abs(target - root.val) < abs(target - res[0]):
                res.popleft()
                res.append(root.val)
            root = root.right
            
        return res