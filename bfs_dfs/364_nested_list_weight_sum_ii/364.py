class Solution:
    # bfs: record the unweighted sum of current level
    #   add such sum every time when going deeper
    
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        from collections import deque
        unweighted, weighted = 0, 0
        nestedList = deque(nestedList)
        while nestedList:
            for i in range(len(nestedList)):
                cur = nestedList.popleft()
                if cur.isInteger():
                    unweighted += cur.getInteger()
                else:
                    nestedList += cur.getList()
            weighted += unweighted
        return weighted
            
     # same as above
#    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
#        unweighted, weighted = 0, 0
#        while nestedList:
#            nextLevel = []
#            for nInt in nestedList:
#                if nInt.isInteger():
#                    unweighted += nInt.getInteger()
#                else:
#                    nextLevel += nInt.getList()
#            weighted += unweighted
#            nestedList = nextLevel
#        return weighted
        
        
    # Another method is to use an array to store the sum of each level
    # add them with weight after knowing the depth of the tree