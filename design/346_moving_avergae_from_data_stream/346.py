from collections import deque
class MovingAverage:
    # add the new val to sum, if nums size exceeds given size, pop and decrement by the first item
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.nums = deque()
        self.sum = 0
        

    def next(self, val: int) -> float:
        if len(self.nums) < self.size:
            self.sum += val
        else:
            self.sum += val - self.nums.popleft()
        self.nums.append(val)
        return self.sum / len(self.nums)
