# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
#        return build(nums, None)
#        
#def build(nums, node):
#    if not nums:
#        return None
#    if not node:
#        node = TreeNode(nums[len(nums) // 2])
#    mid = len(nums) // 2
#    node.left = build(nums[:mid], node.left)
#    node.right = build(nums[mid + 1:], node.right)
#    return node
#

# slicing is costy, so should pass in bounds 
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return build(nums, 0, len(nums) - 1)
        
def build(nums, low, high):
    if not nums:
        return None
    if low > high:
        return None
    mid = low + (high - low) // 2
    node = TreeNode(nums[mid])
    node.left = build(nums, low, mid - 1)
    node.right = build(nums, mid + 1, high)
    return node