
from collections import deque
class NestedIterator:
    # flatten out the entire list when initializing the object
    def __init__(self, nestedList: [NestedInteger]):
        self.q = deque()
        self.flatten(nestedList)
        
    def next(self) -> int:
        return self.q.popleft()
    
    def hasNext(self) -> bool:
        return len(self.q) > 0
    
    def flatten(self, nestedList):
        for nl in nestedList:
            if nl.isInteger():
                self.q.append(nl.getInteger)
            else:
                self.flatten(nl.getList())
                
#    def __init__(self, nestedList: [NestedInteger]):
#        self.q = deque()
#        for nl in nestedList:
#            self.q.append(nl)
#    
#    # when calling next, we just return the first item in the queue
#    def next(self) -> int:
#        return self.q.popleft().getInteger()
#         
#    # when hasNext is called, we flatten out the structure until 
#    # we have a integer as the first item in the queue
#    def hasNext(self) -> bool:
#        while self.q:
#            t = self.q[0]
#            if t.isInteger():
#                return True
#            t = self.q.popleft()
#            for i in range(len(t.getList()) - 1, -1, -1):
#                self.q.appendleft(t.getList()[i])
#        return False
                       