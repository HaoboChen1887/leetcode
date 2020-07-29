class MyQueue:
    # during pop and peek, 
    #   if st2 is empty, 
    #       we pop all numbers from st1 and push onto st2 to maintain the order
    #   otherwise we pop directly from st2
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.st1 = []
        self.st2 = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.st1.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.st2:
            self.shift()
        return self.st2.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.st2:
            self.shift()
        return self.st2[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.st1 and not self.st2
        
    def shift(self):
        while self.st1:
            self.st2.append(self.st1.pop())