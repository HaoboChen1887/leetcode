from collections import deque
class HitCounter:
    # use a queue to record timestamps, check timeout only when getHits
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hitCount = deque()
        self.timeout = 300
        

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.hitCount.append(timestamp)
        

    def getHits(self, timestamp: int) -> int:
        while self.hitCount and timestamp - self.hitCount[0] >= 300:
            self.hitCount.popleft()
        return len(self.hitCount)
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        

        # Follow up
        # we need 2 map of size 300
        # hits[timestamp % 300] records if the timestamps are same or not
        # if the timestamps are the same we increment hits[timestamp % 300] accordingly
        # we getHits are requested, we add up everything in hits that is not timed out