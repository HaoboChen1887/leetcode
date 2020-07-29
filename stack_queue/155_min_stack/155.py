class MinStack:

    # when pushing values, if x <= min_val, push current min_val onto the stack for record
    #   then update min_val
    # when poping, if the top values is min_val, we pop it out and reverse min_val to the next top value
    #   because we maintained the stack in a way such that if min_val is updated, it is always followed 
    #   by the next smallest value
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_1 = sys.maxsize
        self.st = []
        

    def push(self, x: int) -> None:
        if x <= self.min_1:
            self.st.append(self.min_1)
            self.min_1 = x
        self.st.append(x)
        

    def pop(self) -> None:
        tmp = self.st.pop()
        if tmp == self.min_1:
            self.min_1 = self.st.pop()
        

    def top(self) -> int:
        return self.st[-1]
        

    def getMin(self) -> int:
        return self.min_1