# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        findPath(root, res, [], sum)
        return res

def findPath(root, path_list, path, sum):
    if not root.left and not root.right and root.val == sum:
        path.append(root.val)
        path_list.append(path)
    if root.left:
        findPath(root.left, path_list, path + [root.val], sum - root.val)
    if root.right:
        findPath(root.right, path_list, path + [root.val], sum - root.val)