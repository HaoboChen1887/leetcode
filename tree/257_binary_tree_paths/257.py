# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        return findPaths(root, [], '')
        
def findPaths(root: TreeNode, paths: List, path: str):
    if not root.left and not root.right:
        path += str(root.val)
        paths.append(path)
        return paths
    path += str(root.val)
    if root.left:
        findPaths(root.left, paths, path + '->')
    if root.right:
        findPaths(root.right, paths, path + '->')
    print(paths)
    return paths