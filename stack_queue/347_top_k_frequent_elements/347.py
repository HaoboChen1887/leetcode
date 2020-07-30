import heapq
from collections import defaultdict
class Solution:
    # use a map to record frequency, build a maxheap, pop k times
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = defaultdict(int)
        for num in nums:
            m[num] += 1
        m = [(-m[key], key) for key in m]
        heapq.heapify(m)
        res = []
        for i in range(k):
            res.append(heapq.heappop(m)[1])
        return res