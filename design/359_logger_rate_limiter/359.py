from collections import defaultdict
class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = defaultdict(int)
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message in self.m and abs(timestamp - self.m[message]) < 10:
            return False
        self.m[message] = timestamp
        return True
        

