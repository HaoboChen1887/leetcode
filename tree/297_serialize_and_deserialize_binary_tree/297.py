# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        q, res = collections.deque([root]), collections.deque([])
        while root and q:
            curr = q.popleft()
            res.append(curr.val if curr else None)
            if curr:
                q.append(curr.left)
                q.append(curr.right)
        print(res)
        return res
        
    def deserialize(self, data):
        # 如果需要共享指针，可使用queue一类的数据结构辅助
        if not data:
            return None
        res = TreeNode(data.popleft())
        q = collections.deque([res])
        while q and data:
            curr = q.popleft()
            n1 = data.popleft()
            n1 = None if n1 is None else TreeNode(n1)
            if n1:
                curr.left = n1
                q.append(n1)
            n2 = data.popleft()
            n2 = None if n2 is None else TreeNode(n2)
            if n2:
                curr.right = n2
                q.append(n2)
        return res
                
        
#    def serialize(self, root):
#        """Encodes a tree to a single string.
#        :type root: TreeNode
#        :rtype: str
#        """
#        s, res = [root], []
#        while root and s:
#            curr = s.pop()
#            res.append(curr)
#            if curr:
#                s.append(curr.right)
#                s.append(curr.left)
#        return collections.deque([node.val if node else None for node in res])
#        
#
#    def deserialize(self, data):
#        """Decodes your encoded data to tree.
#        
#        :type data: str
#        :rtype: TreeNode
#        """
#        if not data:
#            return None
#        curr = data.popleft()
#        node = None if curr is None else TreeNode(curr)
#        if curr is not None:
#            node.left = self.deserialize(data)
#            node.right = self.deserialize(data)
#        return node
            
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))