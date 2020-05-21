# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.st = []
        self.curr = root
        while self.curr:
            self.st.append(self.curr)
            self.curr = self.curr.left
        
    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.curr = self.st.pop()
        res = self.curr.val
        if self.curr.right:
            self.curr = self.curr.right
            while self.curr:
                self.st.append(self.curr)
                self.curr = self.curr.left
        return res
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.st) != 0
        