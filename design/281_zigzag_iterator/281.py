from collections import deque
class ZigzagIterator:
#    def __init__(self, v1: List[int], v2: List[int]):
#        self.i = 0
#        self.v = []
#        n1, n2 = len(v1), len(v2)
#        size = max(n1, n2)
#        for i in range(size):
#            if i < n1:
#                self.v.append(v1[i])
#            if i < n2:
#                self.v.append(v2[i])
#
#    def next(self) -> int:
#        self.i += 1
#        return self.v[self.i - 1]
#        
#    def hasNext(self) -> bool:
#        return self.i < len(self.v)

    # Follow up: we need a queue to store the lists and return their values in order
    def __init__(self, v1: List[int], v2: List[int]):
        self.q = deque()   
        if v1:
            self.q.append(v1)
        if v2:
            self.q.append(v2)
        
    def next(self) -> int:
        nxt = self.q.popleft()
        if len(nxt) - 1 > 0:
            self.q.append(nxt[1:])
        return nxt[0]

    def hasNext(self) -> bool:
        return len(self.q) > 0