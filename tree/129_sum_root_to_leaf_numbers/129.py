#使用迭代解类似问题时，可把每个节点各自的值分别存在节点内部，而不是用全局变量

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#    def sumNumbers(self, root: TreeNode) -> int:
#        if not root:
#            return 0
#        return addNumbers(root, [0], '')[0]
#    
#def addNumbers(node, sum, num):
#    if not node:
#        return sum
#    num += str(node.val)
#    print(num)
#    if not node.left and not node.right:
#        sum[0] += int(num)
#        print(sum)
#        return sum
#    addNumbers(node.left, sum, num)
#    addNumbers(node.right, sum, num)
#    return sum

#    def sumNumbers(self, root: TreeNode) -> int:
#        return DFS(root, 0)
#        
#def DFS(node, sum):
#    if not node:
#        return 0
#    sum = sum * 10 + node.val
#    if not node.left and not node.right:
#        return sum
#    return DFS(node.left, sum) + DFS(node.right, sum)

    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        s = [root]
        res = 0
        while root and s:
            curr = s.pop()
            if not curr.right and not curr.left:
                res += curr.val
            if curr.right:
                curr.right.val += curr.val * 10
                s.append(curr.right)
            if curr.left:
                curr.left.val += curr.val * 10
                s.append(curr.left)
        return res
