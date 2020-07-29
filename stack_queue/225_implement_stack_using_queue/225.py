from collections import deque
class MyStack:
    # push: enque new elements to the nonempty queue
    # pop: deque from the nonempty queue until only one element is left, the remaining is stack top
    # top: same as pop, but need to deque the remaining and enque to the other queue after peek
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = deque()
        self.q2 = deque()
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if not self.q2:
            self.q1.append(x)
        else:
            self.q2.append(x)
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.shift():
            return self.q1.popleft()
        else:
            return self.q2.popleft()
        

    def top(self) -> int:
        """
        Get the top element.
        """
        res = None
        if self.shift():
            res = self.q1[0]
            self.q2.append(self.q1.popleft())
        else:
            res = self.q2[0]
            self.q1.append(self.q2.popleft())
        return res
    

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.q1 and not self.q2
        
    def shift(self) -> bool:
        if not self.q2:
            while len(self.q1) > 1:
                self.q2.append(self.q1.popleft())
            return True
        else:
            while len(self.q2) > 1:
                self.q1.append(self.q2.popleft())
            return False